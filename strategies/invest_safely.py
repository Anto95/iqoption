import os
import pandas as pd
import numpy as np


def read_stats():
    stocks_stats = {}
    stock_stats_path = "../resources/stock_statistics"
    for file in os.listdir(stock_stats_path):
        stock_ticker = file[:-4]
        stock_stats_df = pd.read_csv(os.path.join(stock_stats_path, file), index_col = 0)
        stocks_stats[stock_ticker] = stock_stats_df
    return stocks_stats

stocks_stats = read_stats()
mon_grw_tickets = []
mon_fll_tickets = []
no_los_buy = []
no_los_sll = []
for ticker in stocks_stats.keys():
    stock = stocks_stats[ticker]
    if(abs(stock.loc["delta"].one_year) > 0.4 > abs(stock.loc["delta"].six_months) > abs(
            stock.loc["delta"].one_quarter) > abs(stock.loc["delta"].one_trimestre) > abs(
        stock.loc["delta"].one_bimestre) > abs(stock.loc["delta"].one_month) > abs(
        stock.loc["delta"].two_weeks)):
        mon_grw_tickets.append(ticker)
    if (abs(stock.loc["delta"].one_year) < - 0.4 < abs(stock.loc["delta"].six_months) < abs(
            stock.loc["delta"].one_quarter) < abs(stock.loc["delta"].one_trimestre) < abs(
        stock.loc["delta"].one_bimestre) < abs(stock.loc["delta"].one_month) < abs(
        stock.loc["delta"].two_weeks)):
        mon_fll_tickets.append(ticker)

        # >= 22 -> two years
        # >= 21 -> one year
        # >= 20 -> six months
        # >= 19 -> four months
        # >= 18 -> three months
    if((sum(stock.loc["lower_10"] == 0)*1) >= 20):
        no_los_buy.append(ticker)
    if((sum(stock.loc["upper_10"] == 0)*1) >= 20):
        no_los_sll.append(ticker)

print("Monotonic growing tickets:")
print(mon_grw_tickets)
print("Monotonic falling tickets:")
print(mon_fll_tickets)
print("Buy option not loosing since 6 months:")
print(no_los_buy)
print("Sell option not loosing since 6 months:")
print(no_los_sll)

very_good__rising_tickers = []
very_good__falling_tickers = []
for ticker in no_los_buy:
    if(stocks_stats[ticker].loc["delta"].one_week > 0.02 and
            stocks_stats[ticker].loc["delta"].two_weeks > 0.02 and
            stocks_stats[ticker].loc["delta"].one_month > 0.02 and
            stocks_stats[ticker].loc["delta"].one_bimestre > 0.02):
        very_good__rising_tickers.append(ticker)
for ticker in no_los_sll:
    if(stocks_stats[ticker].loc["delta"].one_week < -0.02 and
            stocks_stats[ticker].loc["delta"].two_weeks < -0.02 and
            stocks_stats[ticker].loc["delta"].one_month < -0.02 and
            stocks_stats[ticker].loc["delta"].one_bimestre < -0.02):
        very_good__falling_tickers.append(ticker)

print("Very good rising tickers:")
print(very_good__rising_tickers)
print("Very good falling tickers")
print(very_good__falling_tickers)


def get_delta_mean(ticker):
    deltas = stocks_stats[ticker].loc["delta"]
    delta_mean = np.mean([deltas.one_trimestre, deltas.one_bimestre, deltas.one_month, deltas.two_weeks, deltas.one_week, deltas.five_days,
                         deltas.three_days])
    return delta_mean

print("Best growing tickers in delta order: ")
growing = mon_grw_tickets + no_los_buy
growing.sort(key = lambda ticker: get_delta_mean(ticker), reverse = True)
print (growing)

print("Best falling tickers in delta order: ")
falling = mon_fll_tickets + no_los_sll
falling.sort(key = lambda ticker: get_delta_mean(ticker), reverse = False)
print (falling)


cows = []
for ticker in no_los_buy:
    if stocks_stats[ticker].loc["upper_10"].one_bimestre > 100:
        cows.append(ticker)

for ticker in no_los_sll:
    if stocks_stats[ticker].loc["lower_10"].one_bimestre > 100:
        cows.append(ticker)
print("COWS: ")
print (cows)
