import argparse
import logging
import yfinance as yf

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("validate_tickers")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--tickers", nargs="+", required=True)
    args = parser.parse_args()
    tickers = args.tickers
    logger.info(f"{len(tickers)} tickers passed.")
    tickers = list(set(tickers))
    logger.info(f"{len(tickers)} unique tickers.")
    data = yf.download(
        tickers=tickers,
        period="1y",
        interval="1h",
        group_by='ticker'
    )


if __name__ == "__main__":
    main()