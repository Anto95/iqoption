import pandas as pd
import numpy as np
import yfinance as yf
import sys

# Compute how much is possible to win with a certain ticker, by selling the stocks once they rised up by i%
# TODO: Make the single ticker variable and pass it as an argument

def get_data(data_period="1mo", data_interval="2m", ticker = "AAPL"):
        data = yf.download(  # or pdr.get_data_yahoo(...
            # tickers list or string as well
            tickers=ticker,
            period=data_period,
            interval=data_interval,
            group_by='ticker'
        )
        return data

def get_win_ratio():

	if len(sys.argv) == 2:
	  ticker = sys.argv[1]
	else:
	  ticker = "AAPL"

	data = get_data(ticker = ticker).Open.values

	for i in range(2,50):
		won = 0
		limit = 0
		expected_growth = i/100
		expected_fall = 0
		future_offset = 240 #(1day training)
		slighting_mean_dim = 60
		for cnt, point in enumerate(data):
			if cnt < data.shape[0]-future_offset and cnt > slighting_mean_dim:
				slighting_mean = np.mean(data[cnt-slighting_mean_dim:cnt])
				if (point <= slighting_mean * (1-expected_fall)):
					if(max(data[cnt:cnt + future_offset]) > point * (1+(expected_growth/5))):
						if cnt > limit:
							won += 1
							limit = cnt + future_offset
		win_ratio = pow((1 + expected_growth - 0.01),won)
		print(i, win_ratio)
		if(win_ratio == 1.0):
			break

if __name__ == "__main__":
	get_win_ratio()