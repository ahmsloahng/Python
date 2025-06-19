# -*- coding: utf-8 -*-
"""
Created on Thu Jun 19 07:43:56 2025

@author: Amlan Ghosh
"""
import pandas as pd
from statsmodel.tsa.holtwinters import ExponentialSmoothing

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
    forecast = fit.forecast(7) # model forecast
    
    