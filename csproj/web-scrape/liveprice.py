import yfinance as yf
from time import sleep



while 1>0:
    stock = yf.Ticker("RELIANCE.NS")
    price = stock.info['currentPrice']
    print(price)
    sleep(2)