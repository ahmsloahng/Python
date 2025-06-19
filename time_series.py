# -*- coding: utf-8 -*-
"""
Created on Thu Jun 19 07:43:56 2025

@author: Amlan Ghosh
"""
import pandas as pd
from statsmodel.tsa.holtwinters import ExponentialSmoothing
from statsmodel.tsa.arima.model import ARIMA
from statsmodel.tsa.statespace.structural import UnobservedComponents

date_col = 'Date'
vol_col = 'Volume'

def statsmodel_models(df):
    '''Input: Dataframe - Date column and Value column'''
    df.set_index(date_col, inplace = True) # set date column to index
    
    '''Covers:
        1. Exponential Smmothing
        2. Winter-Holts
        3. TES
        4. ARIMA
        5. BSTS
    '''
    
    # Exponential Smoothing
    model = ExponentialSmoothing(df[vol_col], trend = 'add') # define the model
    
    # Winter-Holts
    model = ExponentialSmoothing(df[vol_col], seasonal = 'add', 
                                 seasonal_periods = 12) # define the model
    
    # TES
    model = ExponentialSmoothing(df[vol_col], trend = 'add', seasonal = 'add', 
                                 seasonal_periods = 12) # define the model
    
    # ARIMA
    model = ARIMA(df[vol_col], order = (0,0,3)) # define the model
    
    #BSTS
    model = UnobservedComponents(df[vol_col], level = 'local level', 
                                 trend = True, seasonal = 12) # define the model
    fit = model.fit() # model train
    forecast_horizon = 7 # How many months we want to forecast
    forecast = fit.forecast(steps = forecast_horizon) # model forecast
    '''Result contains a df with forecast column and datetime as index'''


    