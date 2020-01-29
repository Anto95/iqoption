import pandas as pd
import os
import sys

def read_stock_statistics():
    stocks_stats = {}
    stock_stats_path = "../resources/stock_statistics"
    for file in os.listdir(stock_stats_path):
        stock_ticker = file[:-4]
        stock_stats_df = pd.read_csv(os.path.join(stock_stats_path, file), index_col = 0)
        stocks_stats[stock_ticker] = stock_stats_df
    return stocks_stats

def read_win_ratio_all_tickers():
	win_ratio_all_tickers_path = "../resources/win_ratio_all_tickers/A_best_gain.csv"
	win_ratio_all_tickers = pd.read_csv(win_ratio_all_tickers_path, index_col = 0)
	return win_ratio_all_tickers

def get_good_safe(safe_degree = 20):
	#Safe_degree set to these values means that this ticker is growing(falling) since:
	# >= 22 -> two years
	# >= 21 -> one year
	# >= 20 -> six months
	# >= 19 -> four months
	# >= 18 -> three months
	stock_stats = read_stock_statistics()
	safe = []
	for ticker in stock_stats.keys():
		stock = stock_stats[ticker]
		if((sum(stock.loc["lower_10"] == 0)*1) >= safe_degree):
			safe.append(ticker)
		#if((sum(stock.loc["upper_10"] == 0)*1) >= safe_degree):
			#safe.append(ticker)
	good = read_win_ratio_all_tickers()
	good_safe = good[good.ticker.isin(safe)]
	return good_safe

if len(sys.argv) == 2:
	safe_degree = int(sys.argv[1])
else:
	safe_degree = 20
good_safe = get_good_safe(safe_degree)
print(good_safe)