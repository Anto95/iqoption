import yfinance as yf
import numpy as np
import pandas as pd
import scipy.stats as sc
import datetime
import os

# Get statistics over last two year of data with different granularities:
#   60 min for data older than 2 months
#   2 min for data older than 7 days
#   1 min for data newer than 7 days

class Stock:
    def __init__(self, ticker):
        self.ticker = ticker
        print("Downloading data for ", self.ticker)
        self.two_years = self.get_2_years_data()
        self.two_months = self.get_60_days_data()
        self.one_week = self.get_7_days_data()
        print((self.two_years.shape,self.two_months.shape,self.one_week.shape))

    def get_data(self, data_period=None, data_interval=None, data_start = None, data_end = None):
        data = yf.download(  # or pdr.get_data_yahoo(...
            # tickers list or string as well
            tickers=self.ticker,
            start = data_start,
            end = data_end,
            period=data_period,
            interval=data_interval,
            group_by='ticker'
        )
        return data

    def get_2_years_data(self):
        data = self.get_data(data_period="2y", data_interval="60m")
        time_series = data["Open"]
        time_series = time_series.dropna(how='all')
        return time_series

    def get_60_days_data(self):
        data = self.get_data(data_period="43d", data_interval="2m")
        time_series = data["Open"]
        time_series = time_series.dropna(how='all')
        return time_series

    def get_7_days_data(self):
        data = self.get_data(data_period="7d", data_interval="1m")
        time_series = data["Open"]
        time_series = time_series.dropna(how='all')
        return time_series

class StockStatistics:
    def __init__(self, stock):
        self.stock = stock
        self.stats = self.compute_stats()
        self.stat_list = ["delta", "end", "start", "max", "min", "mean", "std", "perc_99", "perc_95", "perc_90", "perc_1", "perc_5", "perc_10", "upper_10", "lower_10"]

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
            "one_bimestre": Statistics(self.stock.two_months).get_stat_list(),
            "one_month": Statistics(self.stock.two_months[self.stock.two_months.index > self.stock.two_months.index[
                -1] - datetime.timedelta(days=30)]).get_stat_list(),
            "two_weeks": Statistics(self.stock.two_months[self.stock.two_months.index > self.stock.two_months.index[
                -1] - datetime.timedelta(days=15)]).get_stat_list(),
            "one_week": Statistics(self.stock.one_week).get_stat_list(),
            "five_days": Statistics(self.stock.one_week[self.stock.one_week.index > self.stock.one_week.index[
                -1] - datetime.timedelta(days=5)]).get_stat_list(),
            "three_days": Statistics(self.stock.one_week[self.stock.one_week.index > self.stock.one_week.index[
                -1] - datetime.timedelta(days=3)]).get_stat_list(),
            "two_days": Statistics(self.stock.one_week[self.stock.one_week.index > self.stock.one_week.index[
                -1] - datetime.timedelta(days=2)]).get_stat_list(),
            "one_day": Statistics(self.stock.one_week[self.stock.one_week.index > self.stock.one_week.index[
                -1] - datetime.timedelta(days=1)]).get_stat_list(),
            "twelve_hours": Statistics(self.stock.one_week[self.stock.one_week.index > self.stock.one_week.index[
                -1] - datetime.timedelta(hours=12)]).get_stat_list(),
            "six_hours": Statistics(self.stock.one_week[self.stock.one_week.index > self.stock.one_week.index[
                -1] - datetime.timedelta(hours=6)]).get_stat_list(),
            "three_hours": Statistics(self.stock.one_week[self.stock.one_week.index > self.stock.one_week.index[
                -1] - datetime.timedelta(hours=3)]).get_stat_list(),
            "two_hours": Statistics(self.stock.one_week[self.stock.one_week.index > self.stock.one_week.index[
                -1] - datetime.timedelta(hours=2)]).get_stat_list(),
            "one_hour": Statistics(self.stock.one_week[self.stock.one_week.index > self.stock.one_week.index[
                -1] - datetime.timedelta(hours=1)]).get_stat_list(),
            "thirty_minutes": Statistics(self.stock.one_week[self.stock.one_week.index > self.stock.one_week.index[
                -1] - datetime.timedelta(minutes=30)]).get_stat_list(),
            "fifteen_minutes": Statistics(self.stock.one_week[self.stock.one_week.index > self.stock.one_week.index[
                -1] - datetime.timedelta(minutes=15)]).get_stat_list(),
            "ten_minutes": Statistics(self.stock.one_week[self.stock.one_week.index > self.stock.one_week.index[
                -1] - datetime.timedelta(minutes=10)]).get_stat_list(),
            "five_minutes": Statistics(self.stock.one_week[self.stock.one_week.index > self.stock.one_week.index[
                -1] - datetime.timedelta(minutes=5)]).get_stat_list()
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
                     self.percentiles[9], self.times_upper_10, self.times_lower_10]
        return data_list

def get_stock_statistics(stock_ticker):
    stock = Stock(stock_ticker)
    if(stock):
        stock_statistics = StockStatistics(stock)
    else:
        stock_statistics = None
    return stock_statistics

def get_stock_statistics_df(stock_ticker):
    stock_statistics = get_stock_statistics(stock_ticker)
    stock_stats_df = pd.DataFrame(stock_statistics.stats, index=stock_statistics.stat_list)
    return stock_stats_df

def get_all_stocks_statistics():
    iqoption_tickers = "CAN FTR AMD TSLA DVN WORK AMZN DO FFIV SNAP MANU CMCSA CXO AAPL MELI FMC INTC IDXX EIX ALGN FSLR RTN SPOT COP LMT TWTR BUD AIR DISCA GE" \
                       " AAP MMM EQR GILD FCX CVX UL DOV DVA EFX SU WBA DHR ET EXPD MSFT EZJ ANSS CAT LYG SLB PYPL BMY OR FLS ADBE BAC NKE ETFC EONGY RACE" \
                       " FB COST DHI EBAY BP JPM ACN AA XOM KO AGN RBS EMR NVDA HAS MA GOOGL SYK ESS FITB EXR ADSK DAL EQT TMUS PFE CRM BIDU MU ECL HSBC" \
                       " MS GS FIS TFX AMGN HON CVS CTAS ETR NEE VZ DRE ABBV MCD BYND PM IBM CTXS FISV NFLX QCOM RMD ATVI SBUX VOD CSCO FRT FE ED CL ZM PG DIS DRI BA" \
                       " PST KHC DTE WMT CRON EMN ABT LYFT DLR BBY DFS TEF CTL MDT MO DBX BBVA GM CGC PINS TLRY GWPH ACB".split()
    stocks_stats = {}
    for stock_ticker in iqoption_tickers:
        stock_stats_df = get_stock_statistics_df(stock_ticker)
        if(stock_stats_df.any().any()):
            stocks_stats[stock_ticker] = stock_stats_df
            stock_stats_df.to_csv("../resources/stock_statistics/" + stock_ticker + ".csv")


get_all_stocks_statistics()
#stocks_stats = read_stats()
# Indexes
# two_years, one_year, six_months, one_quarter, one_trimestre, one_bimestre, one_month, two_weeks, one_week, five_days,
# three_days, two_days, one_day, twelve_hours, six_hours, three_hours, two_hours, one_hour, thirty_minutes, fifteen_minutes, ten_minutes, five_minutes
#Columns
#stat_list = ["delta", "end", "start", "max", "min", "mean", "std", "perc_99", "perc_95", "perc_90", "perc_1", "perc_5", "perc_10", "upper_10", "lower_10"]

