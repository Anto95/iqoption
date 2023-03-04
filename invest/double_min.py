import argparse
import logging

from matplotlib import pyplot as plt

from modelling.double_min.double_min import DoubleMin
from utils.paths import td

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("investing")


class Investment:
    def __init__(self, amount, buy_price, sell_price, trailing_stop_loss=None):
        self.amount = amount
        self.open_price = buy_price
        self.trailing_stop_loss = trailing_stop_loss
        self.max_sell_price = sell_price
        self.close_price = None

    def check_close(self, sell_price):
        if self.close_price:
            return 0
        self.max_sell_price = max(self.max_sell_price, sell_price)
        trailing_loss = 1 - sell_price / self.max_sell_price
        if self.trailing_stop_loss and trailing_loss > self.trailing_stop_loss:
            return self.close(sell_price)
        else:
            return 0

    def close(self, sell_price):
        self.close_price = sell_price
        return self.amount * self.close_price


def get_data(tickers, start_date, stop_date):
    data = {}
    for ticker in tickers:
        df = td(ticker)
        if start_date:
            df = df[df.index >= start_date]
        if stop_date:
            df = df[df.index <= stop_date]
        data[ticker] = df.close.values
    return data


def visualize(data, point):
    plt.plot(data[:point.invest_th[0] + 10])
    plt.scatter(*point.first_min, c='b')
    plt.scatter(*point.max_in_interval, c='r')
    plt.scatter(*point.second_min, c='b')
    plt.scatter(*point.invest_th, c='g')
    plt.show()


def investment_simulation(data, dm):
    capital = 3000
    placement = 100
    investments = []
    n_points = len(data)
    for i in range(n_points):
        buy_price = data[i] * 1.01
        sell_price = data[i] * 0.99
        if i % 100 == 0:
            projected_capital = capital + sum(investment.amount * sell_price
                                              for investment in investments
                                              if not investment.close_price)
            logger.info(f"Processing {i} / {n_points} - Projected capital: {projected_capital}")
        for investment in investments:
            closed = investment.check_close(sell_price)
            if closed != 0:
                capital += closed
                logger.info(f"{str(i).zfill(5)} - investment closed - Capital: {capital}.")
        for j in range(dm.last_min_window_atleast, dm.last_min_window_atmost + dm.after_double_min_atmost):
            i_start = i - j
            point = dm.detect(data[i_start:i])
            # if point:
            #     print(i_start + point.invest_th[0], i_start, point.invest_th[0], i)
            #     visualize(data[i_start:i], point)
            if point and i_start + point.invest_th[0] == i - 1:
                capital -= placement
                amount = placement / buy_price
                new_investment = Investment(amount, buy_price, sell_price, trailing_stop_loss=0.03)
                investments.append(new_investment)
                logger.info(f"{str(i).zfill(5)} - investment opened - Capital: {capital}.")
                break
    print(capital)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--tickers", nargs="+", help="List of tickers on which to invest.")
    parser.add_argument("--start-date", help="%Y-%m-%d %H:%M:%S")
    parser.add_argument("--stop-date", help="%Y-%m-%d %H:%M:%S")
    args = parser.parse_args()
    data = get_data(args.tickers, args.start_date, args.stop_date)
    logging.getLogger("double_min").setLevel(logging.ERROR)
    data = data["TSLA"]
    dm = DoubleMin(
                 last_min_window_atleast=10,
                 last_min_window_atmost=500,
                 after_double_min_atmost=150,
                 double_min_tolerance=0.0005,
                 down_after_double_min_tolerance=0.0001,
                 up_after_double_min_tolerance=0.0001,
                 double_min_dim_atleast=0.02
    )
    # For optimization, it is much faster to start from the past. (x600 times faster)


if __name__ == "__main__":
    main()
