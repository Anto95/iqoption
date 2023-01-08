import os
import argparse
import logging
from datetime import datetime, timedelta
import pandas as pd
import yfinance as yf

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("update_dataset")
price_dataset_path = os.path.join("data/price_dataset")
dataset_cols = ['date', 'ticker', 'open', 'high', 'low', 'close', 'adj_close', 'volume', 'dividends', 'stock_splits']

"""
Keep saved a dataset with the prices evolution of all the tickets with a 2 min granularity.
Do not run when the stock exchange is opened otherwise you will loose a part of data.
"""


class EmptyResponse(Exception):
    pass


def get_period(interval):
    end = datetime.now()
    limits = {"1m": 8, "2m": 60, "5m": 60, "15m": 60, "30m": 60, "60m": 60, "90m": 60, "1h": 730}
    if interval in limits:
        start = end - timedelta(days=limits[interval] - 1)
    else:
        start = datetime(1970, 1, 1, 0, 0, 0)
    return start, end


def get_data(data_interval=None, tickers=None):
    start, end = get_period(data_interval)
    data = yf.download(
        tickers=tickers,
        start=start,
        end=end,
        interval=data_interval,
        group_by='ticker',
        actions=True
    ).stack(0).reset_index()
    if data.empty:
        logger.info("Terminating as empty dataframe retrieved.")
        raise EmptyResponse
    if len(data.columns) == 11:
        data = data.drop('Capital Gains', axis=1)
    data.columns = ['date', 'ticker', 'adj_close', 'close', 'dividends', 'high', 'low', 'open', 'stock_splits', 'volume']
    data = data[dataset_cols]
    return data


def get_history(tickers, data_interval):
    dfs = []
    for ticker in tickers:
        data_path = os.path.join(price_dataset_path, data_interval, f"{ticker}.csv")
        if os.path.isfile(data_path):
            old_data = pd.read_csv(data_path)
            old_data["ticker"] = ticker
            old_data["date"] = pd.to_datetime(old_data["date"], format="%Y-%m-%d %H:%M:%S")
            old_data = old_data[dataset_cols]
            dfs.append(old_data)
    if dfs:
        old_data = pd.concat(dfs)
    else:
        old_data = None
    return old_data


def add_history(data, tickers, data_interval):
    old_data = get_history(tickers, data_interval)
    if old_data is not None:
        data = pd.concat([old_data, data]).drop_duplicates(subset=["date", "ticker"]).sort_values("date")
    return data


def write_data(data, tickers, data_interval):
    data_dir = os.path.join(price_dataset_path, data_interval)
    if not os.path.isdir(data_dir):
        os.makedirs(data_dir)
    for ticker in tickers:
        ticker_path = os.path.join(data_dir, f"{ticker}.csv")
        ticker_data = data[data.ticker == ticker].drop("ticker", axis=1)
        ticker_data.to_csv(ticker_path, index=None, date_format='%Y-%m-%d %H:%M:%S')
    return


def update_price_dataset(tickers, interval):
    logger.info("Updating pricing dataset for {tickers}...")
    data = get_data(tickers=tickers, data_interval=interval)
    data = add_history(data, tickers=tickers, data_interval=interval)
    write_data(data=data, tickers=tickers, data_interval=interval)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--tickers", required=True)
    parser.add_argument("-v", "--verbose", action="store_true")
    parser.add_argument("-i", "--interval", default="5m",
                        choices=["1m", "2m", "5m", "15m", "30m", "60m", "90m", "1h", "1d", "5d", "1wk", "1mo", "3mo"])
    args = parser.parse_args()
    if args.verbose:
        logger.setLevel("DEBUG")
    update_price_dataset(args.tickers, args.interval)


if __name__ == "__main__":
    main()
