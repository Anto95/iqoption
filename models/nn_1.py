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
# Strategy: Use stock history of a set of shares to predict on another set of shares. Train the model with regression
# Result --> Very poor, no significant prediction

iqoption_tickers = "CAN FTR AMD TSLA DVN WORK AMZN DO FFIV SNAP MANU CMCSA CXO AAPL MELI FMC INTC IDXX EIX ALGN UBE FSLR RTN SPOT COP LMT MKS TWTR BUD AIR DISCA MRW GE AAP MMM EQR GILD FCX CVX UL DOV DVA EFX RR HEIO SU WBA DHR ET EXPD MSFT EZJ ANSS CAT LYG SLB PYPL BMY OR FLS PIRC ADBE BAC NKE BLT ETFC EONGY RACE FB TKA MRCG COST DHI EBAY BP JPM ACN AA XOM KO AGN RBS EMR NVDA SIE HAS MA GOOGL SYK ESS FITB EXR ADSK DAL EQT TMUS PFE CRM BIDU FBHS ALVG MU ECL HSBC MS GS FIS TFX CON AMGN HON CVS CTAS ETR NEE VZ DRE ABBV MCD BYND PM IBM CTXS FISV NFLX QCOM RMD ATVI SBUX VOD CSCO FRT FE FDJ ED CL ZM PG DIS TI DRI BA PST KHC DTE WMT CRON EMN ABT LYFT DLR BBY DFS TEF CTL MDT CBK MO DBX BBVA JUVE GM CGC PINS TLRY GWPH ACB"
#iqoption_tickers = "CAN FTR AMD TSLA DVN"

class model():

	def __init__(self):
		super().__init__()
		self.build()
		self.nn.summary()

	def build(self):

		x = Input(shape=(220,))

		input_layer = Reshape((220,1)) (x)

		conv = Conv1D(64, 3, activation='relu', input_shape = (220,1)) (input_layer)

		conv = Conv1D(32, 3, activation='relu', input_shape = (220,1)) (conv)

		conv = Conv1D(16, 3, activation='relu') (conv)

		flattened = Flatten() (conv)

		dense = Dense(5, activation='relu' )(flattened)

		input_layer = input_layer [:,180:,:]

		conv = Conv1D(16, 3, activation='relu') (input_layer)

		conv = Conv1D(4, 3, activation='relu') (input_layer)

		dense_1 = Dense(30, activation='relu' )(flattened)

		merged = Concatenate()([dense, dense_1])

		#dense_1 = Dense(220, activation='relu')(flattened)

		dense = Dense(30, activation=None )(merged)
		

		self.nn = Model(inputs=x, outputs=dense_1)

		#self.nn = Sequential()

		#self.nn.add(Reshape((220,1)))

		#self.nn.add(Conv1D(32, 3, 
		#          activation='relu', 
		#          input_shape=(220,1)))

		#self.nn.add(Conv1D(16, 3, 
		#          activation='relu'))

		#self.nn.add(Conv1D(8, 3, 
		#          activation='relu'))

		#self.nn.add(Conv1D(4, 3, 
		#          activation='relu'))

		#self.nn.add(Flatten())

		#self.nn.add(Dense(30))
		self.nn.compile(optimizer='adam',loss='mse')


data = yf.download(  # or pdr.get_data_yahoo(...
        # tickers list or string as well
        tickers = iqoption_tickers,

        # use "period" instead of start/end
        # valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
        # (optional, default is '1mo')
        period = "ytd",

        # fetch data by interval (including intraday if period < 60 days)
        # valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
        # (optional, default is '1d')
        interval = "1d",

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


time_series = data.xs('Open', axis=1, level=1, drop_level=True)
time_series = time_series.dropna(axis=0, how='all').dropna(axis = 1)
prices = np.transpose(time_series.values)
X_train = prices[:120,:220] # 120x220
Y_train = prices[:120,220:] # 120x31
X_test = prices[120:,:220] # 26x220
Y_test = prices[120:,220:] # 26x31
model = model()
model.nn.fit(X_train,Y_train, validation_split = 0, nb_epoch = 100, batch_size = 1)
Y_pred = model.nn.predict(X_test)
mse = 0
for cnt, y_pred in enumerate(Y_pred):
	y_test = Y_test[cnt]
	df=pd.DataFrame({'x': range(1,31), 'y1': y_test, 'y2': y_pred })
	# multiple line plot
	plt.plot( 'x', 'y1', data=df, color='green', linewidth=4)
	plt.plot( 'x', 'y2', data=df, color='blue', linewidth=2)
	plt.show()
	mse += mean_squared_error(y_pred, y_test)
mse = mse/len(Y_pred)
print(mse)

