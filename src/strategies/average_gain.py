import pandas as pd
import os
import sys
import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt

def get_data(data_period="1mo", data_interval="60m", ticker = "AAPL"):
        data = yf.download(  # or pdr.get_data_yahoo(...
            # tickers list or string as well
            tickers=ticker,
            period=data_period,
            interval=data_interval,
            group_by='ticker'
        )
        return data
def compute_stats_time_to_gain(ticker, gain, time_window):
	time_needed = []
	data = get_data(ticker = ticker, data_period = time_window).Open.values
	for cnt, point in enumerate(data):
		for i in range(cnt,len(data)):
			value = data[i]
			expected = point * (1 + (gain / 5))
			if value >= expected:
				time_needed.append((i-cnt)/8)
				break
	avgt=np.mean(time_needed)
	maxt=np.max(time_needed)
	mint=np.min(time_needed)
	stdt=np.std(time_needed)
	time_needed = []
	gain = gain + 0.00087 * (maxt + int(maxt/5)*2)
	for cnt, point in enumerate(data):
		if (cnt < len(data) - (maxt*8)):
			for i in range(cnt,len(data)):
				value = data[i]
				expected = point * (1 + (gain / 5))
				if value >= expected:
					time_needed.append((i-cnt)/8)
					break
	success=float(len(time_needed))/float(len(data) - maxt*8)
	avgt=np.mean(time_needed)
	maxt=np.max(time_needed)
	mint=np.min(time_needed)
	stdt=np.std(time_needed)
	quantile_80 = np.quantile(time_needed, 0.8, interpolation = 'higher')
	return avgt, maxt, mint, stdt, quantile_80, success, time_needed

def get_one_ticker(ticker, gain, time_window):
	avgt, maxt, mint, stdt, quantile_80, success, time_dist = compute_stats_time_to_gain(ticker, gain, time_window)
	print("{} --> Success Rate: {}, Average: {}, Quantile_80: {}, Max: {}, Min: {}, Standard Deviation: {}".format(ticker, success, avgt, quantile_80, maxt, mint, stdt))
	plt.hist(time_dist, density = True, cumulative = True, bins = 1000, range = (0,20))
	plt.title('Cumulative count of optained gain of {} on {}'.format(gain, ticker))
	plt.xlabel('Days')
	plt.ylabel('Cumulative count')
	plt.show()

def get_tickers_comparison(tickers, gain, time_windows):
	to_df = []
	for ticker in tickers:
		for time_window in time_windows:
			to_df.append([ticker] + [time_window] + list(compute_stats_time_to_gain(ticker, gain, time_window)[:-1]))
	df = pd.DataFrame(to_df, columns = ["ticker","time_window","average","max","min","std","quantile_80","success"])
	return df

tickers = ["ATVI", "ETR", "BMY" , "MDT", "AAPL", "DHR", "NVDA", "MSFT"]
gain = 0.04
time_windows = ["6mo"]
df = get_tickers_comparison(tickers, gain, time_windows)
print(df.groupby('ticker').mean().sort_values( by = ["max","quantile_80","average"]))

# ticker= "AAPL"
# gain = 0.04
# time_window = "1mo"
# if len(sys.argv) == 4:
# 	ticker = sys.argv[1]
# 	gain = float(sys.argv[2])
# 	time_window = sys.argv[3]
# get_one_ticker(ticker, gain, time_window)