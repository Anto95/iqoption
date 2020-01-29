import yfinance as yf
import pandas as pd
import os
import sys
import datetime
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

# Date format: yyyy-mm-dd
today = get_today()
for ticker in iqoption_tickers:
	start_date, old_data, old_data_path = read_history(ticker)
	if(start_date != today.strftime('%Y-%m-%d')):
		end_date = (today + datetime.timedelta(days=1)).strftime('%Y-%m-%d') # Tomorrow
		print("Getting data for " + ticker + " from " + start_date + " to " + end_date + "...")
		data = get_data(data_interval = "2m", data_start = start_date, data_end = end_date, ticker = ticker)
		data = data["Open"].dropna(how='all')
		appendData(data, old_data, old_data_path)





