import yfinance as yf
import pandas as pd
import tensorflow as tf
import numpy as np
from sklearn.metrics import mean_squared_error
import keras
import random
from tensorflow.keras.models import Sequential, Model
from tensorflow.keras.layers import Conv1D, Dense, Reshape, Flatten, Input, Concatenate, Add, Multiply
import tensorflow.keras.backend as K
import matplotlib.pyplot as plt

# 1D Conv Net
# Strategy: For each stock, iterate over the date history and create a dataset of [past,future] samples
#			and use it to train the model. This time, each sample is labelled with a 0 or a 1, saying if the investement
#           would have been profitable or not.
# Result --> Very poor, no significant prediction

iqoption_tickers = "CAN FTR AMD TSLA DVN WORK AMZN DO FFIV SNAP MANU CMCSA CXO AAPL MELI FMC INTC IDXX EIX ALGN UBE FSLR RTN SPOT COP LMT MKS TWTR BUD AIR DISCA MRW GE AAP MMM EQR GILD FCX CVX UL DOV DVA EFX RR HEIO SU WBA DHR ET EXPD MSFT EZJ ANSS CAT LYG SLB PYPL BMY OR FLS PIRC ADBE BAC NKE BLT ETFC EONGY RACE FB TKA MRCG COST DHI EBAY BP JPM ACN AA XOM KO AGN RBS EMR NVDA SIE HAS MA GOOGL SYK ESS FITB EXR ADSK DAL EQT TMUS PFE CRM BIDU FBHS ALVG MU ECL HSBC MS GS FIS TFX CON AMGN HON CVS CTAS ETR NEE VZ DRE ABBV MCD BYND PM IBM CTXS FISV NFLX QCOM RMD ATVI SBUX VOD CSCO FRT FE FDJ ED CL ZM PG DIS TI DRI BA PST KHC DTE WMT CRON EMN ABT LYFT DLR BBY DFS TEF CTL MDT CBK MO DBX BBVA JUVE GM CGC PINS TLRY GWPH ACB"
#iqoption_tickers = "CAN FTR AMD TSLA DVN WORK AMZN DO FFIV SNAP MANU CMCSA CXO AAPL"


class ModelStocks:

    def __init__(self):

        super().__init__()
        self.build()

    def build(self):

        x = Input(shape=(1440,))

        input_layer = Reshape((1440, 1))(x)

        conv = Conv1D(16,3,activation='relu',input_shape=(1440,1)) (input_layer)

        conv = Conv1D(8, 3,activation='relu') (conv)

        flatten = Flatten() (conv)

        dense = Dense(4, activation='relu')(flatten)

        output = Dense(1, activation = 'sigmoid')(dense)

        self.nn = Model(inputs = x, outputs = output)

        self.nn.summary()

        self.nn.compile(optimizer='adam', loss='binary_crossentropy', metrics= ["acc"])


def get_data():
    data = yf.download(  # or pdr.get_data_yahoo(...
        # tickers list or string as well
        tickers=iqoption_tickers,

        # use "period" instead of start/end
        # valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
        # (optional, default is '1mo')
        period="1y",

        # fetch data by interval (including intraday if period < 60 days)
        # valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
        # (optional, default is '1d')
        interval="60m",

        # group by ticker (to access via data['SPY'])
        # (optional, default is 'column')
        group_by='ticker',

        # adjust all OHLC automatically
        # (optional, default is False)
        auto_adjust=True,

        # download pre/post regular market hours data
        # (optional, default is False)
        prepost=True,

        # use threads for mass downloading? (True/False/Integer)
        # (optional, default is True)
        threads=True,

        # proxy URL scheme use use when downloading?
        # (optional, default is None)
        proxy=None
    )
    return data


def create_train_test(time_series):
    predicted_time_window = 24  # hours
    train_time_window = 1440  # hours
    test_time_window = 100  # hours
    min_data_points = 3000  # hours
    spread = 0.01
    stocks = time_series.columns
    train_dim = int(stocks.shape[0] * 0.8)  # stocks
    train_stocks = stocks[random.sample(range(1, stocks.shape[0]), train_dim)]
    test_stocks = np.array(list(set(stocks) - set(train_stocks)))
    lost = 0
    won = 0
    wise_choice = 0
    too_wise_choice = 0
    for stock in train_stocks:
        prices = time_series[stock].fillna(method='ffill').dropna(axis=0, how='all').values
        data_points = prices.shape[0]
        if (data_points > min_data_points):
            X = []
            Y = []
            # Create Training Set
            for i in range(0, data_points - (predicted_time_window + train_time_window + test_time_window),
                           10):
                price_history = prices[i:i + train_time_window]
                price_to_predict = prices[i + train_time_window:i + predicted_time_window + train_time_window]
                X.append(price_history)
                Y_init = price_history[-1] * (1 + spread)
                gain = 5*(price_to_predict / Y_init -1)
                to_win = 0.15
                to_lose = - 0.5
                if(max(gain) >= to_win and min(gain) >= to_lose):
                    Y.append(1)
                else:
                    Y.append(0)
            X_train = np.array(X)
            Y_train = np.array(Y)

            # Create Test Set
            price_history = prices[data_points - (train_time_window + predicted_time_window):data_points - predicted_time_window]
            price_to_predict = prices[data_points - predicted_time_window:]
            X_test = np.expand_dims(np.array(price_history), axis=0)
            Y_init = price_history[-1] * (1 + spread)
            gain = 5 * (price_to_predict / Y_init - 1)
            to_win = 0.03
            to_lose = - 0.5
            Y_test = []
            if (max(gain) >= to_win and min(gain) >= to_lose):
                Y_test.append(1)
            else:
                Y_test.append(0)
            model = ModelStocks()
            model.nn.fit(X_train, Y_train, validation_split=0.2, nb_epoch=30, batch_size=16)
            Y_pred = model.nn.predict(X_test, batch_size=1)
            Y_pred = int(Y_pred > 0.5)
            Y_test = Y_test[0]
            print(Y_pred, Y_test)
            if(Y_pred == Y_test and Y_pred == 1):
                won += 1
            if (Y_pred == Y_test and Y_pred == 0):
                wise_choice += 1
            if (Y_pred != Y_test and Y_pred == 0):
                too_wise_choice += 1
            if (Y_pred != Y_test and Y_pred == 1):
                lost += 1
            print("Won: ", won, "Lost: ", lost, "Wise_choice: ", wise_choice, "Too_wise_choice: ", too_wise_choice)




data = get_data()
time_series = data.xs('Open', axis=1, level=1, drop_level=True)
print("Data preparation...")
time_series = time_series.dropna(axis=1, how='all')
create_train_test(time_series)
random.seed(5000)
