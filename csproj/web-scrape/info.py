import yfinance as yf

goog = yf.Ticker("GOOGL")

summary = goog.info['longBusinessSummary']

