# New Python

# install libraries
import yfinance as yf
import pandas as pd
import numpy as np

# get/set working directory
import os

os.getcwd()


# Set up data
dat = yf.Ticker("MSFT")
tickerInfo = dir(dat)
dat.info
dat.calendar
dat._price_history
dat._shares
dat.analyst_price_targets
dat.quarterly_income_stmt
dat.history(period="1mo")
dat.option_chain(dat.options[0]).calls


# inputs
# static parameters
# wrangling
# Exploratory
# Initial automated methods
# Validation of automated methods
