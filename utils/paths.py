import os

import pandas as pd

BASE_PATH = "C:/Users/Antonio/Desktop/work/datasets/yahoo"
BASE_PATH = sorted(
    [os.path.join(BASE_PATH, file) for file in os.listdir(BASE_PATH)],
    key=lambda f: os.path.getmtime(f)
)[-1]


def tp(ticker, granularity="2m"):
    return os.path.join(BASE_PATH, granularity, ticker) + ".csv"


def td(ticker, granularity="2m"):
    path = tp(ticker, granularity)
    df = pd.read_csv(path)
    df = df[["date", "close"]].set_index("date")
    return df
