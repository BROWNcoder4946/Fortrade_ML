import yfinance as yf
import pandas as pd

# Specify the forex pair, e.g., 'EURUSD=X' for Euro to USD
forex_pair = 'EURUSD=X'

# Fetching historical data
historical_data = yf.download(forex_pair, start="2014-01-01", end="2023-12-31", interval='1d')
# Convert this data to csv
historical_data.to_csv('EURUSD_hr_data')

# Fetching validation data
validation_data = yf.download(forex_pair, start="2024-01-01", end="2024-08-21", interval='1d')
# Convert this data to csv
validation_data.to_csv('Validation_data')