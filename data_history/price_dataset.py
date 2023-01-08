import os
import argparse
import logging
from datetime import datetime, timedelta
import pandas as pd
import yfinance as yf

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("price_dataset")
price_dataset_path = os.path.join("data/price_dataset")

"""
Keep saved a dataset with the prices evolution of all the tickets with a 2 min granularity.
Do not run when the stock exchange is opened otherwise you will loose a part of data.
"""


def get_data(data_interval=None, ticker=None):
    data = yf.download(
        tickers=ticker,
        period="max",
        interval=data_interval,
        group_by='ticker',
        actions=True
    ).reset_index()
    if data.empty:
        logger.info("Terminating as empty dataframe retrieved.")
        raise Exception
    data.columns = ['date', 'open', 'high', 'low', 'close', 'adj_close', 'volume', 'dividends', 'stock_splits']
    return data


def get_history(ticker, interval):
    data_path = os.path.join(price_dataset_path, interval, f"{ticker}.csv")
    if os.path.isfile(data_path):
        old_data = pd.read_csv(data_path)
        old_data["date"] = pd.to_datetime(old_data["date"], format="%Y-%m-%d %H:%M:%S")
        start_date = old_data["date"].values[-1].astype('M8[ms]').astype('O') + timedelta(days=1)
    else:
        start_date = 'max'
        old_data = None
    return start_date, old_data, data_path


def append_data(data, old_data, data_path):
    data_dir = os.path.dirname(data_path)
    if not os.path.isdir(data_dir):
        os.makedirs(data_dir)
    if old_data is not None:
        data = pd.concat([old_data, data]).drop_duplicates(subset="date").sort_values("date")
        data.to_csv(data_path, index=None, date_format='%Y-%m-%d %H:%M:%S')
    else:
        data.to_csv(data_path, index=None, date_format='%Y-%m-%d %H:%M:%S')
    return


def update_price_dataset(iqoption_tickers, interval):
    logger.info("Updating pricing dataset...")
    end_date = datetime.today()
    for ticker in iqoption_tickers:
        start_date, old_data, data_path = get_history(ticker, interval)
        logger.info(f"Getting data for {ticker} from {start_date} to {end_date}...")
        data = get_data(data_interval=interval, ticker=ticker)
        append_data(data, old_data, data_path)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbose", action="store_true")
    parser.add_argument("-i", "--interval", default="5m",
                        choices=["1m", "2m", "5m", "15m", "30m", "60m", "90m", "1h", "1d", "5d", "1wk", "1mo", "3mo"])
    args = parser.parse_args()
    if args.verbose:
        logger.setLevel("DEBUG")
    iqoption_tickers = "CAN FTR AMD TSLA DVN WORK AMZN DO FFIV SNAP MANU CMCSA CXO AAPL MELI FMC INTC IDXX EIX ALGN" \
                       " FSLR RTN SPOT COP LMT TWTR BUD AIR DISCA GE AAP MMM EQR GILD FCX CVX UL DOV DVA EFX SU WBA" \
                       " DHR ET EXPD MSFT EZJ ANSS CAT LYG SLB PYPL BMY OR FLS ADBE BAC NKE ETFC EONGY RACE FB COST" \
                       " DHI EBAY BP JPM ACN AA XOM KO AGN RBS EMR NVDA HAS MA GOOGL SYK ESS FITB EXR ADSK DAL EQT" \
                       " TMUS PFE CRM BIDU MU ECL HSBC MS GS FIS TFX AMGN HON CVS CTAS ETR NEE VZ DRE ABBV MCD BYND" \
                       " PM IBM CTXS FISV NFLX QCOM RMD ATVI SBUX VOD CSCO FRT FE ED CL ZM PG DIS DRI BA PST KHC DTE" \
                       " WMT CRON EMN ABT LYFT DLR BBY DFS TEF CTL MDT MO DBX BBVA GM CGC PINS TLRY GWPH ACB".split()
    iqoption_tickers = ["AAPL", "AMZN", "GOOGL"]
    update_price_dataset(iqoption_tickers, args.interval)


if __name__ == "__main__":
    main()
