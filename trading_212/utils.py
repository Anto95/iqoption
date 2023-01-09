from selenium import webdriver
from pytrading212 import *
driver = webdriver.Chrome()


def get_trading_212(username, password):
    return Trading212(username, password, driver, mode=Mode.DEMO)


def buy_stock(trading212, instrument_code, quantity):
    trading212.execute_order(MarketOrder(instrument_code=instrument_code, quantity=quantity))


def sell_stock(trading212, instrument_code, quantity):
    trading212.execute_order(MarketOrder(instrument_code=instrument_code, quantity=-quantity))

