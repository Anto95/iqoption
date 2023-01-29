import logging
import datetime
import random

import numpy as np
import pandas as pd
from frozendict import frozendict
from matplotlib import pyplot as plt

logger = logging.getLogger(__name__)
logger.setLevel("DEBUG")


def plot_stock(df, n_ticks=10):
    df["high"].plot()
    x = [int(df.shape[0] / n_ticks) * i for i in range(n_ticks)] + [df.shape[0] - 1]
    plt.xticks(x, labels=df["date"].values[x], rotation=45)
    plt.show()


def data_prep(df):
    df.columns = ['date', 'open', 'high', 'low', 'close', 'volume', 'dividends', 'stock_splits']
    df["date"] = df["date"].str[:10]
    return df


def plot_capital_evolution(capital_evolution, n_ticks=10, ticker=""):
    plt.title(f"Applying double min strategy to {ticker}")
    plt.plot([capital for date, capital in capital_evolution])
    if n_ticks > len(capital_evolution):
        plt.xticks(range(len(capital_evolution)), labels=[date for date, capital in capital_evolution], rotation=45)
    else:
        x = [int(len(capital_evolution) / n_ticks) * i for i in range(n_ticks)] + [len(capital_evolution) - 1]
        plt.xticks(x, labels=[capital_evolution[i][0] for i in x], rotation=45)
    plt.show()


def double_min_simulation(params=frozendict({"last_min_window_atleast":30, "last_min_window_atmost":90,
                                  "after_double_min_atmost":45, "double_min_tolerance":0.005,
                                  "down_after_double_min_tolerance":0.01, "double_min_dim_atleast":0.05,
                                  "trailing_loss_perc":0.02})):

    last_min_window_atleast = params["last_min_window_atleast"]
    last_min_window_atmost = params["last_min_window_atmost"]
    after_double_min_atmost = params["after_double_min_atmost"]
    double_min_tolerance = params["double_min_tolerance"]
    down_after_double_min_tolerance = params["down_after_double_min_tolerance"]
    double_min_dim_atleast = params["double_min_dim_atleast"]
    trailing_loss_perc = params["trailing_loss_perc"]
    tickers = ['AA', 'AAL', 'AAP', 'AAPL', 'AB', 'ABBV', 'ABT', 'ABX', 'ACAD', 'ACIW', 'ACN', 'ACOR', 'ADBE', 'ADI']
    tickers = ["AAPL", "AMZN", "GOOGL", "MSFT"]
    t_tickers = {}
    capital = 3000
    for ticker in tickers:
        t = dict()
        t["df"] = data_prep(pd.read_csv(f"data/{ticker}.csv"))
        # INITIAL PARAMTERS
        t["start_date"] = t["df"]["date"].values[0]
        t["capital_evolution"] = [[t["start_date"], capital]]
        t["double_min"] = False
        t["position_opened"] = False
        t["previous_min"] = 0
        t["double_min_idx"] = 0
        t["position_opened_idx"] = 0
        t["previous_max"] = 0
        t["stocks"] = 0
        t["old_capital"] = capital
        t["n_double_mins"] = 0
        t["n_position_opened"] = 0
        t["n_position_closed"] = 0
        t_tickers[ticker] = t

    start_investing = datetime.datetime.strptime("1962-01-02", "%Y-%m-%d")
    date = start_investing
    dates = []
    while date < datetime.datetime.now():
        date += datetime.timedelta(days=1)
        dates.append(date)
    for i_date, date in enumerate(dates):
        random.shuffle(tickers)
        for ticker in tickers:
            t = t_tickers[ticker]
            initial_date = datetime.datetime.strptime(t["df"]["date"][0], "%Y-%m-%d")
            i = (date - initial_date).days
            if i < 0 or i >= t["df"].shape[0]:
                continue
            if t["position_opened"]:
                if t["df"]["low"].values[i] <= (1 - trailing_loss_perc) * t["df"]["high"].values[t["position_opened_idx"]: i].max():
                    capital = round(t["stocks"] * t["df"]["low"].values[i], 2)
                    # sell_price = round(df["low"].values[i], 5)
                    t["position_opened"] = False
                    t["double_min"] = False
                    # gain = round(capital - t["old_capital"], 2)
                    # gain_word = "Gain" if gain > 0 else "Loss"
                    t["n_position_closed"] += 1
                    # print(f"{date} - {n_position_closed} position closed! Sold {stocks} at {sell_price} - New capital {capital} - {gain_word}: {gain}")
                    t["old_capital"] = capital
                    t["capital_evolution"].append([date, capital])
                else:
                    pass
            elif t["double_min"]:
                if t["df"]["high"].values[i] >= t["previous_max"]:
                    t["position_opened"] = True
                    t["position_opened_idx"] = i
                    t["stocks"] = round(capital / t["df"]["high"].values[i], 2)
                    t["n_position_opened"] += 1
                    # buy_price = round(t["df"]['high'].values[i], 5)
                    # print(f"{date} - {n_position_opened} opened position! Bought {stocks} stocks at {buy_price}.")
                elif (i - t["double_min_idx"] >= after_double_min_atmost or
                    t["previous_min"] - t["df"]["low"][i] >= down_after_double_min_tolerance * t["previous_min"]):
                    t["double_min"] = False
                else:
                    pass

            else:
                t["previous_min_idx"] = i - np.argmin(t["df"]["low"].values[max(i - last_min_window_atmost, 0):i+1])
                t["previous_min"] = t["df"]["low"].values[t["previous_min_idx"]]
                t["previous_max"] = t["df"]["high"].values[max(i - last_min_window_atmost, 0):i+1].max()
                if (
                        i > 0 and
                        np.abs(t["df"].low.values[i] - t["previous_min"]) <= double_min_tolerance * t["previous_min"] and
                        i - t["previous_min_idx"] >= last_min_window_atleast and
                        (t["previous_max"] - t["previous_min"])/t["previous_max"] > double_min_dim_atleast
                ):
                    t["n_double_mins"] += 1
                    t["double_min"] = True
                    t["double_min_idx"] = i
                    #print(f"{date} - {n_double_mins} double min found! Dates [{df['date'][previous_min_idx]},{df['date'][i]}].")
        capital
    #plot_capital_evolution(capital_evolution)
    return - capital


params = {'after_double_min_atmost': 424, 'double_min_dim_atleast': 0.04418881214416712,
          'double_min_tolerance': 0.049237885221764366, 'down_after_double_min_tolerance': 0.02923469253853918,
          'last_min_window_atleast': 98, 'last_min_window_atmost': 106, 'trailing_loss_perc': 0.020633404269757006}

#df = data_prep(pd.read_csv("data/AAPL.csv"))
#plot_stock(df)
double_min_simulation(params=frozendict(params))
