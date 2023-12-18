import yfinance as yf
from time import sleep


stock = yf.Ticker("RELIANCE.NS")
while 1>0:
    
    price = stock.fast_info['last_price']
    print(price)
    sleep(2)