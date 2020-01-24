import yfinance as yf
import pandas as pd
import tensorflow as tf
import numpy as np
from sklearn.metrics import mean_squared_error
import keras
from tensorflow.keras.models import Sequential, Model
from tensorflow.keras.layers import Conv1D, Dense, Reshape, Flatten, Input, Concatenate, Add
import tensorflow.keras.backend as K
import matplotlib.pyplot as plt

# 1D Conv Net
# Strategy: For each stock, iterate over the date history and create a dataset of [past,future] samples
#			and use it to train the model. Train the model with regression.
# Result --> Very poor, no significant prediction

iqoption_tickers = "CAN FTR AMD TSLA DVN WORK AMZN DO FFIV SNAP MANU CMCSA CXO AAPL MELI FMC INTC IDXX EIX ALGN UBE FSLR RTN SPOT COP LMT MKS TWTR BUD AIR DISCA MRW GE AAP MMM EQR GILD FCX CVX UL DOV DVA EFX RR HEIO SU WBA DHR ET EXPD MSFT EZJ ANSS CAT LYG SLB PYPL BMY OR FLS PIRC ADBE BAC NKE BLT ETFC EONGY RACE FB TKA MRCG COST DHI EBAY BP JPM ACN AA XOM KO AGN RBS EMR NVDA SIE HAS MA GOOGL SYK ESS FITB EXR ADSK DAL EQT TMUS PFE CRM BIDU FBHS ALVG MU ECL HSBC MS GS FIS TFX CON AMGN HON CVS CTAS ETR NEE VZ DRE ABBV MCD BYND PM IBM CTXS FISV NFLX QCOM RMD ATVI SBUX VOD CSCO FRT FE FDJ ED CL ZM PG DIS TI DRI BA PST KHC DTE WMT CRON EMN ABT LYFT DLR BBY DFS TEF CTL MDT CBK MO DBX BBVA JUVE GM CGC PINS TLRY GWPH ACB"
iqoption_tickers = "CAN FTR AMD TSLA DVN WORK AMZN DO FFIV SNAP MANU CMCSA CXO AAPL"

class model_stocks():

	def __init__(self):
		super().__init__()
		self.build()
		#self.nn.summary()

	def build(self):

		self.nn = Sequential()

		self.nn.add(Reshape((1440,1)))

		self.nn.add(Conv1D(32, 3, 
		          activation='relu', 
		          input_shape=(1440,1)))

		self.nn.add(Conv1D(16, 3, 
		          activation='relu'))


		self.nn.add(Flatten())

		self.nn.add(Dense(24, activation=None))

		self.nn.compile(optimizer='adam',loss='mse')


data = yf.download(  # or pdr.get_data_yahoo(...
        # tickers list or string as well
        tickers = iqoption_tickers,

        # use "period" instead of start/end
        # valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
        # (optional, default is '1mo')
        period = "1y",

        # fetch data by interval (including intraday if period < 60 days)
        # valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
        # (optional, default is '1d')
        interval = "60m",

        # group by ticker (to access via data['SPY'])
        # (optional, default is 'column')
        group_by = 'ticker',

        # adjust all OHLC automatically
        # (optional, default is False)
        auto_adjust = True,

        # download pre/post regular market hours data
        # (optional, default is False)
        prepost = True,

        # use threads for mass downloading? (True/False/Integer)
        # (optional, default is True)
        threads = True,

        # proxy URL scheme use use when downloading?
        # (optional, default is None)
        proxy = None
    )

predicted_time_window = 24 # hours
train_time_window = 1440 # hours
test_time_window = 100
time_series = data.xs('Open', axis=1, level=1, drop_level=True)
time_series = time_series.dropna(axis=1, how = 'all')
train_stocks = time_series.columns
print("Training and testing")
for stock in train_stocks:
	prices = time_series[stock].fillna(method='ffill').dropna(axis=0, how = 'all').values
	data_points = prices.shape[0]
	if(data_points > 3000 and np.mean(prices)>10):
		X = []
		Y = []
		#Create Training Set
		for i in range (0,data_points-(predicted_time_window + train_time_window+test_time_window),test_time_window):
			X.append(prices[i:i+train_time_window])
			Y.append(prices[i+train_time_window:i+predicted_time_window + train_time_window])
		X_train = np.array(X)
		Y_train = np.array(Y)
		X = []
		Y = []
		#Create Test Set
		X_test = np.expand_dims(np.array(prices[data_points-(train_time_window + predicted_time_window):data_points-predicted_time_window]), axis=0)
		Y_test = np.expand_dims(np.array(prices[data_points-predicted_time_window:]), axis=0)
		print(X_train.shape, Y_train.shape, X_test.shape, Y_test.shape)

		model = model_stocks()
		model.nn.fit(X_train,Y_train, validation_split = 0.2, nb_epoch = 100, batch_size = 16)
		Y_pred = model.nn.predict(X_test, batch_size=1)
		Y_test_plot = np.concatenate([prices[:data_points-predicted_time_window],np.squeeze(Y_test)])[-100:]
		Y_pred_plot = np.concatenate([prices[:data_points-predicted_time_window],np.squeeze(Y_pred)])[-100:]
		print(Y_test_plot[-30:])
		print(Y_pred_plot[-30:])
		df=pd.DataFrame({'x': range(1,100+1), 'y1': Y_test_plot, 'y2': Y_pred_plot })
		# multiple line plot
		plt.plot( 'x', 'y1', data=df, color='green', linewidth=4)
		plt.plot( 'x', 'y2', data=df, color='blue', linewidth=2)
		plt.show()

