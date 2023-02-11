import argparse
import numpy as np
from matplotlib import pyplot as plt
from conf import download_conf
from data_history.update_dataset import get_data

monitored_tickers = download_conf.tickers


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--threshold", help="Provide a threshold to decide when the alerting should be triggered."
                        , default=1)
    parser.add_argument("--email-addresses", nargs='+', default=[])
    data = get_data(data_interval='1d', tickers=monitored_tickers)
    high_volumes = []
    for i, ticker in enumerate(monitored_tickers):
        if i % 50 == 0:
            print(f"{i} / {len(monitored_tickers)} tickers analyzed.")
        if data.date.values[-1] != np.datetime64('today'):
            continue
        volumes = data[data.ticker == ticker].volume.values
        plt.title(f"Evoluzione dei volumi degli ultimi 90 giorni di {ticker}")
        plt.plot(volumes[-91:], label="Volume Giornaliero")
        plt.hlines(y=volumes[-91:-1].mean(), xmin=0, xmax=91, label="Media 90g", colors='y', linestyles='dashed')
        plt.hlines(y=volumes[-91:-1].mean() * 4, xmin=0, xmax=91, label="4 * Media 90g", colors='orange', linestyles='dashed')
        plt.hlines(y=volumes[-91:-1].max(), xmin=0, xmax=91, label="Massimo 90g", colors='r', linestyles='dashed')
        plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05),
          fancybox=True, shadow=True, ncol=5)
        plt.show()
        previous_max = volumes[-91:-1].max()
        diff = volumes[-1] - previous_max
        if diff > 0:
            high_volumes.append([ticker, round(diff / previous_max, 4)])
    high_volumes = sorted(high_volumes, key=lambda x: -x[1])
    print(high_volumes)


if __name__ == "__main__":
    main()
