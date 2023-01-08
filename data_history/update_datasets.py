import argparse
import os
import logging

from conf.download_conf import tickers, intervals
from data_history.update_dataset import update_price_dataset, EmptyResponse

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("update_datasets")
logging.getLogger("update_dataset").setLevel(logging.ERROR)

"""
Run update dataset for all tickers and for all intervals in conf/download_conf.py
"""


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--tickers", default=tickers)
    parser.add_argument("-i", "--intervals", nargs="+", default=intervals)
    parser.add_argument("-v", "--verbose", action="store_true")
    args = parser.parse_args()
    for i, interval in enumerate(args.intervals):
        logger.info(f"Updating dataset for interval {interval} ({i+1}/{len(intervals)}).")
        try:
            update_price_dataset(args.tickers, interval)
        except EmptyResponse:
            pass


if __name__ == "__main__":
    main()
