import yfinance as yf
import pandas as pd
goog = yf.Ticker("AAPL")

df = goog.history(interval='1d', start="2022-12-01", end = "2022-12-15")
print(df)