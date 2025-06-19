# -*- coding: utf-8 -*-
"""
Created on Thu Jun 19 07:43:56 2025

@author: Amlan Ghosh
"""
import pandas as pd
from statsmodel.tsa.holtwinters import ExponentialSmoothing
from statsmodel.tsa.arima.model import ARIMA

date_col = 'Date'
vol_col = 'Volume'

'''Winter-Holts Method'''
def winter_holts(df):
    '''Input: Dataframe - Date column and Value column'''
    df.set_index(date_col, inplace = True) # set date column to index
    model = ExponentialSmoothing(df[vol_col], seasonal = 'add', 
                                 seasonal_periods = 12) # define the model
    fit = model.fit() # model train
    forecast_horizon = 7 # How many months we want to forecast
    forecast = fit.forecast(steps = forecast_horizon) # model forecast
    '''Result contains a df with forecast column and datetime as index'''

def arima(df):
    '''Input: Dataframe - Date column and Value column'''
    df.set_index(date_col, inplace = True) # set date column to index
    model = ARIMA(df[vol_col], order = (0,0,3)) # define the model
    fit = model.fit() # model train
    forecast_horizon = 7 # How many months we want to forecast
    forecast = fit.forecast(steps = forecast_horizon) # model forecast
    '''Result contains a df with forecast column and datetime as index'''

def exp_smooth(df):
    '''Input: Dataframe - Date column and Value column'''
    df.set_index(date_col, inplace = True) # set date column to index
    model = ExponentialSmoothing(df[vol_col], trend = 'add') # define the model
    fit = model.fit() # model train
    forecast_horizon = 7 # How many months we want to forecast
    forecast = fit.forecast(steps = forecast_horizon) # model forecast
    '''Result contains a df with forecast column and datetime as index'''    
    