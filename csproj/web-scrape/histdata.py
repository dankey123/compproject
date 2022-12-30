import yfinance as yf
import pandas as pd
goog = yf.Ticker("GOOG")

df = goog.history(interval='1d', start="2022-12-01", end = "2022-12-15")

df= df(nrows =5)

print(df)