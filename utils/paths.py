import os

BASE_PATH = "C:/Users/Antonio/Desktop/work/datasets/yahoo"
BASE_PATH = sorted(
    [os.path.join(BASE_PATH, file) for file in os.listdir(BASE_PATH)],
    key=lambda f: os.path.getmtime(f)
)[-1]


def tp(ticker, granularity="2m"):
    return os.path.join(BASE_PATH, granularity, ticker) + ".csv"

