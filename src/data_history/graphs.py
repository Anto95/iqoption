import pandas as pd
import matplotlib.pyplot as plt
import sys
import os
import shutil
from datetime import timedelta, date
import os
import glob
import price_dataset

# Generate graphs with data trend with day of the week as a title
# Todo: Adapt to all the months of the year

def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)

def get_graphs(ticker, start_date):
	ticker_data = pd.read_csv("../resources/price_dataset/" + ticker + ".csv", index_col = 0)
	fig_path = os.path.join("../resources/graphs", ticker)
	if(not os.path.isdir(fig_path)):
		os.mkdir(fig_path)
	for single_date in daterange(start_date, date.today()):
		day_of_week = single_date.strftime("%A")
		if (day_of_week not in ["Saturday", "Sunday"]):
			data = ticker_data[ticker_data.index <= (single_date + timedelta(days=1)).strftime("%Y-%m-%d")]
			data = data[data.index >= single_date.strftime("%Y-%m-%d")]
			plt.plot(data.values)
			plt.title(day_of_week)
			plt.savefig(os.path.join(fig_path, single_date.strftime("%Y-%m-%d") + "_" + day_of_week) + ".png")
			plt.close()

def get_all_graphs():
	#price_dataset.update_price_dataset()
	print("Creating daily graphs...")
	if(os.path.isdir("../resources/graphs/AAPL")):
		list_of_files = glob.glob('../resources/graphs/AAPL/*') # * means all if need specific format then *.csv
		latest_file = max(list_of_files, key=os.path.getctime)
		start_date = latest_file.split('/')[-1].split('_')[0]
	else:
		start_date = "2020-01-01"
	start_date = date(*map(int, start_date.split('-')))
	iqoption_tickers =	"CAN FTR AMD TSLA DVN WORK AMZN DO FFIV SNAP MANU CMCSA CXO AAPL MELI FMC INTC IDXX EIX ALGN FSLR RTN SPOT COP LMT TWTR BUD AIR DISCA GE" \
						" AAP MMM EQR GILD FCX CVX UL DOV DVA EFX SU WBA DHR ET EXPD MSFT EZJ ANSS CAT LYG SLB PYPL BMY OR FLS ADBE BAC NKE ETFC EONGY RACE" \
						" FB COST DHI EBAY BP JPM ACN AA XOM KO AGN RBS EMR NVDA HAS MA GOOGL SYK ESS FITB EXR ADSK DAL EQT TMUS PFE CRM BIDU MU ECL HSBC" \
						" MS GS FIS TFX AMGN HON CVS CTAS ETR NEE VZ DRE ABBV MCD BYND PM IBM CTXS FISV NFLX QCOM RMD ATVI SBUX VOD CSCO FRT FE ED CL ZM PG DIS DRI BA" \
						" PST KHC DTE WMT CRON EMN ABT LYFT DLR BBY DFS TEF CTL MDT MO DBX BBVA GM CGC PINS TLRY GWPH ACB".split()
	for cnt, ticker in enumerate(iqoption_tickers):
		get_graphs(ticker, start_date)

if __name__ == "__main__":
	get_all_graphs()