import pandas as pd
import numpy as np
import yfinance as yf

# Compute how much is possible to win with a certain ticker, by selling the stocks once they rised up by i%
# TODO: Make the single ticker variable and pass it as an argument

def get_data(data_period="1mo", data_interval="2m"):
        data = yf.download(  # or pdr.get_data_yahoo(...
            # tickers list or string as well
            tickers="AAPL",
            period=data_period,
            interval=data_interval,
            group_by='ticker'
        )
        return data
def get_win_ratio():
	#TODO: Define data
	data = get_data().Open.values

	for i in range(1,30):
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
		print(i, pow((1 + expected_growth - 0.01),won))

if __name__ == "__main__":
	get_win_ratio()