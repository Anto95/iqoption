import yfinance as yf
import pandas as pd
import os
import sys
import datetime

#Get the winning potential ratio with a variable "take profit" threshold for all the tickers available in iqoption
#Write the result of all of them in  a csv and create a file with the leaderboard of best winning tickers in last 2 months
home_dir = "../resources"
price_dataset_path = os.path.join(home_dir,"price_dataset")
min_date = "2020-01-01"

def get_data(data_interval=None, data_start = None, data_end = None, ticker = None):
        data = yf.download(  # or pdr.get_data_yahoo(...
            # tickers list or string as well
            tickers = ticker,
            start = data_start,
            end = data_end,
            interval = data_interval,
            group_by = 'ticker'
        )
        return data

iqoption_tickers = "CAN FTR AMD TSLA DVN WORK AMZN DO FFIV SNAP MANU CMCSA CXO AAPL MELI FMC INTC IDXX EIX ALGN FSLR RTN SPOT COP LMT TWTR BUD AIR DISCA GE" \
                       " AAP MMM EQR GILD FCX CVX UL DOV DVA EFX SU WBA DHR ET EXPD MSFT EZJ ANSS CAT LYG SLB PYPL BMY OR FLS ADBE BAC NKE ETFC EONGY RACE" \
                       " FB COST DHI EBAY BP JPM ACN AA XOM KO AGN RBS EMR NVDA HAS MA GOOGL SYK ESS FITB EXR ADSK DAL EQT TMUS PFE CRM BIDU MU ECL HSBC" \
                       " MS GS FIS TFX AMGN HON CVS CTAS ETR NEE VZ DRE ABBV MCD BYND PM IBM CTXS FISV NFLX QCOM RMD ATVI SBUX VOD CSCO FRT FE ED CL ZM PG DIS DRI BA" \
                       " PST KHC DTE WMT CRON EMN ABT LYFT DLR BBY DFS TEF CTL MDT MO DBX BBVA GM CGC PINS TLRY GWPH ACB".split()

def read_history(ticker):
	old_data_path = os.path.join(price_dataset_path, (ticker + ".csv"))
	if os.path.isfile(old_data_path):
		old_data = pd.read_csv(old_data_path, index_col = 0, header = None, names = [0])
		start_date = old_data.index[-1][:10]
	else:
		start_date = min_date
		old_data = None
	return start_date, old_data, old_data_path

def appendData(data, old_data, old_data_path):
	if(old_data is not None):
		updated_data = pd.concat([old_data,data])#.drop_duplicates().reset_index(drop=True) # To check
		os.remove(old_data_path)
		updated_data.to_csv(old_data_path, header = False)
	else:
		data.to_csv(old_data_path, header = False)
	return

def get_today():
	today = (datetime.datetime.today())
	return today



def get_strategy_data():
	strategy = {}
	for ticker in iqoption_tickers:
		file_path = os.path.join("../resources/win_ratio_all_tickers", ticker) + ".csv"
		if(os.path.isfile(file_path)):
			os.remove(file_path)
		today = get_today()
		end_date = (today + datetime.timedelta(days=1)).strftime('%Y-%m-%d') # Tomorrow
		data = get_data(data_interval = "2m", data_start = today-datetime.timedelta(days = 55), data_end = end_date, ticker = ticker)
		data = data.Open.values[1:]
		stats = []
		for i in range(1,50):
			buy = 0 
			count = 0
			fail_count = 0
			gain = i
			factor = (1 +((gain + 1)/500))
			for point in data:
				if(buy != 0 and (point > (buy * factor))):
					count += 1
					buy = point
				elif(buy == 0):
					buy = point
				if(point < buy * 0.9):
					fail_count += 1
			win_factor = pow(1 + (gain/100),count)
			stats.append([ticker, gain, count,win_factor,fail_count])
		stats_df = pd.DataFrame(stats, columns = ["ticker", "gain", "count", "win_factor","fail_count"])
		stats_df.to_csv(file_path)
		strategy[ticker] = stats_df
	return strategy


strategy = get_strategy_data()
max_inv = 0
max_ticker = None
stats = []
for ticker in strategy.keys():
	df = strategy[ticker]
	if(max(df.fail_count) == 0):
		max_earn = max(df.win_factor)
		stats.append([ticker,max_earn])


stats.sort(key = lambda x: x[1], reverse=True)
stats = pd.DataFrame(stats, columns = ["ticker","best_gain"])
stats.to_csv(os.path.join("../resources/win_ratio_all_tickers", "A_best_gain") + ".csv")