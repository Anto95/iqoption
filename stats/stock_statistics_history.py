import yfinance as yf
import numpy as np
import pandas as pd
import scipy.stats as sc
import datetime
import os

# This module create an history of statistics over 2 years of data using a slighting window of 1 month
# The goal is to have the statistics updated to date, considering date as the beginning of each month of 2019.

class Stock:
    def __init__(self, ticker, start, end):
        self.ticker = ticker
        self.start = start
        self.end = end
        print("Downloading data for ", self.ticker)
        self.two_years = self.get_2_years_data()

    def get_data(self, data_period=None, data_interval=None, data_start = None, data_end = None):
        data = yf.download(  # or pdr.get_data_yahoo(...
            # tickers list or string as well
            tickers=self.ticker,
            start = data_start,
            end = data_end,
            interval=data_interval,
            group_by='ticker'
        )
        return data
    def subtract_days(self, date_str, nb_days):
        print(date_str)
        date = datetime.date(
            year = int(date_str[:4]),
            month = int(date_str[5:7]),
            day = int(date_str[8:10])
        )
        sub = date - datetime.timedelta(days = nb_days)
        result = str(sub)
        return result

    def get_2_years_data(self):
        start_data = self.start
        data = self.get_data(data_start = start_data, data_end = self.end, data_interval="1d")
        time_series = data["Open"]
        time_series = time_series.dropna(how='all')
        return time_series

class StockStatisticsHistory:
    def __init__(self, stock):
        self.stock = stock
        self.stats = self.compute_stats()
        self.stat_list = ["delta", "end", "start", "max", "min", "mean", "std", "perc_99", "perc_95", "perc_90", "perc_1", "perc_5", "perc_10", "upper_10", "lower_10", "percentiles"]

    def compute_stats(self):
        print("Computing stock_statistics for ", self.stock.ticker)
        stats = {
            "two_years": Statistics(self.stock.two_years).get_stat_list(),
            "one_year": Statistics(self.stock.two_years[
                                       self.stock.two_years.index > self.stock.two_years.index[-1] - datetime.timedelta(
                                           days=365)]).get_stat_list(),
            "six_months": Statistics(self.stock.two_years[self.stock.two_years.index > self.stock.two_years.index[
                -1] - datetime.timedelta(days=183)]).get_stat_list(),
            "one_quarter": Statistics(self.stock.two_years[self.stock.two_years.index > self.stock.two_years.index[
                -1] - datetime.timedelta(days=122)]).get_stat_list(),
            "one_trimestre": Statistics(self.stock.two_years[self.stock.two_years.index > self.stock.two_years.index[
                -1] - datetime.timedelta(days=91)]).get_stat_list(),
            "one_bimestre": Statistics(self.stock.two_years).get_stat_list(),
            "one_month": Statistics(self.stock.two_years[self.stock.two_years.index > self.stock.two_years.index[
                -1] - datetime.timedelta(days=30)]).get_stat_list(),
            "two_weeks": Statistics(self.stock.two_years[self.stock.two_years.index > self.stock.two_years.index[
                -1] - datetime.timedelta(days=15)]).get_stat_list(),
            "one_week": Statistics(self.stock.two_years).get_stat_list(),
            "five_days": Statistics(self.stock.two_years[self.stock.two_years.index > self.stock.two_years.index[
                -1] - datetime.timedelta(days=5)]).get_stat_list(),
            "three_days": Statistics(self.stock.two_years[self.stock.two_years.index > self.stock.two_years.index[
                -1] - datetime.timedelta(days=3)]).get_stat_list(),
            "two_days": Statistics(self.stock.two_years[self.stock.two_years.index > self.stock.two_years.index[
                -1] - datetime.timedelta(days=2)]).get_stat_list(),
            "one_day": Statistics(self.stock.two_years[self.stock.two_years.index > self.stock.two_years.index[
                -1] - datetime.timedelta(days=1)]).get_stat_list()
        }
        return stats

class Statistics:
    def __init__(self, data):
        super().__init__()
        self.data = data
        self.start = 0
        self.end = 0
        self.delta = 0
        self.max = 0
        self.min = 0
        self.mean = 0
        self.mode = 0
        self.std_ = 0
        self.var = 0
        self.percentiles = []
        self.times_upper_10 = 0
        self.times_lower_10 = 0
        self.compute_statistics()

    def compute_statistics(self):
        self.start = self.data[0]
        self.end = self.data[-1]
        self.delta = self.end / self.start - 1
        self.max = np.max(self.data)
        self.min = np.min(self.data)
        self.mean = np.mean(self.data)
        self.mode = sc.mode(self.data)
        self.std = np.std(self.data)
        self.var = np.var(self.data)
        self.percentiles = np.percentile(self.data,range(1,100))
        for cnt in range(self.data.shape[0]):
            if ((self.data[cnt:] >= self.data[cnt] * 1.1).any()):
                self.times_upper_10 += 1
            if ((self.data[cnt:] <= self.data[cnt] * 0.9).any()):
                self.times_lower_10 += 1

    def get_stat_list(self):
        data_list = [self.delta, self.end, self.start, self.max, self.min, self.mean, self.std, self.percentiles[98],
                     self.percentiles[94], self.percentiles[89], self.percentiles[0], self.percentiles[4],
                     self.percentiles[9], self.times_upper_10, self.times_lower_10, self.percentiles]
        return data_list

def get_stock_statistics(stock_ticker, start, end):
    stock = Stock(stock_ticker, start, end)
    if(stock.two_years.any()):
        stock_statistics = StockStatisticsHistory(stock)
    else:
        stock_statistics = None
    return stock_statistics

def get_stock_statistics_df(stock_ticker, start, end):
    stock_statistics = get_stock_statistics(stock_ticker, start, end)
    if (stock_statistics):
        stock_stats_df = pd.DataFrame(stock_statistics.stats, index=stock_statistics.stat_list)
    else:
        stock_stats_df = pd.DataFrame()
    return stock_stats_df

def get_all_stocks_statistics(start = None, end = None):
    if(start and end):
        output_path = os.path.join("../resources/stock_statistics_history", start + "_" + end)
        if(not os.path.isdir(output_path)):
            os.mkdir(output_path)
        iqoption_tickers = "CAN FTR AMD TSLA DVN WORK AMZN DO FFIV SNAP MANU CMCSA CXO AAPL MELI FMC INTC IDXX EIX ALGN FSLR RTN SPOT COP LMT TWTR BUD AIR DISCA GE" \
                           " AAP MMM EQR GILD FCX CVX UL DOV DVA EFX SU WBA DHR ET EXPD MSFT EZJ ANSS CAT LYG SLB PYPL BMY OR FLS ADBE BAC NKE ETFC EONGY RACE" \
                           " FB COST DHI EBAY BP JPM ACN AA XOM KO AGN RBS EMR NVDA HAS MA GOOGL SYK ESS FITB EXR ADSK DAL EQT TMUS PFE CRM BIDU MU ECL HSBC" \
                           " MS GS FIS TFX AMGN HON CVS CTAS ETR NEE VZ DRE ABBV MCD BYND PM IBM CTXS FISV NFLX QCOM RMD ATVI SBUX VOD CSCO FRT FE ED CL ZM PG DIS DRI BA" \
                           " PST KHC DTE WMT CRON EMN ABT LYFT DLR BBY DFS TEF CTL MDT MO DBX BBVA GM CGC PINS TLRY GWPH ACB".split()
        stocks_stats = {}
        for stock_ticker in iqoption_tickers:
            stock_stats_df = get_stock_statistics_df(stock_ticker, start, end)
            if(not stock_stats_df.empty):
                stocks_stats[stock_ticker] = stock_stats_df
                stock_stats_df.to_csv(os.path.join(output_path, stock_ticker + ".csv"))
    else:
        print("Please precise a valid interval")

def read_stats():
    stocks_stats = {}
    for file in os.listdir("../resources/stock_statistics"):
        stock_ticker = file[:-4]
        stock_stats_df = pd.read_csv(os.path.join("../resources/stock_statistics", file), index_col = 0)
        stocks_stats[stock_ticker] = stock_stats_df
    return stocks_stats


def create_histories_stocks_stats():
    for i in range (9,13):
        start_date = "2017-" + str(i).zfill(2) + "-" + "01"
        end_date = "2019-" + str(i).zfill(2)  + "-" + "01"
        print("Processing step ", start_date, end_date)
        get_all_stocks_statistics(start_date, end_date)




#get_all_stocks_statistics()
create_histories_stocks_stats()

