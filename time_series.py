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

from statsmodel.tsa.statespace.sarimax import SARIMAX
from scipy.fftpack import fft

def fourier_poisson_sarimax(df):
    
    # Fourier transformation
    values = df['Column'].values
    fft_values = fft(values)
    frequencies = np.fft.fftfreq(len(values))
    dominant_frequencies = frequencies[np.argsort(np.abs(fft_values))[-3:]]
    for freq in dominant_frequencies:
        df[f'sin_{freq}'] = np.sin(2 * np.pi * freq * np.arange(len(df)))
        df[f'cos_{freq}'] = np.cos(2 * np.pi * freq * np.arange(len(df)))
    
    # SARIMAX
    forecast_steps = 7
    last_date = df.index[-1]
    future_dates = pd.date_range(start = last_date, periods = forecast_steps + 1,
                                 freq = 'MS')[1:]
    future_exog = pd.DataFrame(index = future_dates)    
    for freq in dominant_frequencies[:1]:
        future_exog[f'sin_{freq}'] = np.sin(2 * np.pi * freq * np.arange(
            len(df), len(df) + forecast_steps))
        future_exog[f'cos_{freq}'] = np.cos(2 * np.pi * freq * np.arange(
            len(df), len(df) + forecast_steps))
    model = SARIMAX(df['Column'], order = (1,0,1), seasonal_order = (1,0,1,12),
                    exog = df[[f'sin_{dominant_frequencies[0]}', 
                               f'cos_{dominant_frequencies[0]}']],
                    family = 'poisson')
    fit = model.fit() # model train
    forecast = fit.forecast(steps = forecast_steps, exog = future_exog) # model forecast    
    '''Result contains a df with forecast column and datetime as index'''
    
'''Transformations'''
from scipy.stats import boxcox
from scipy.special import inv_boxcox

def scipy_transformations(df):
    
    '''Covers:
        1. Boxcox
    '''
    
    # Boxcox transformation
    df['Transformed Column'], lam = boxcox(df['Column'])
    df['Column'] = inv_boxcox(df['Transformed Column'], lam)

from sklearn.preprocessing import PowerTransformer

def sklearn_transformation(df):
    
    '''Covers:
        1. Yeo-Johnson
    '''
    
    # Yeo-Johnson transformation
    
    # Transformation
    transformer = PowerTransformer(method = 'yeo-johnson', standardize = False)
    transformed_column = transformer.fit_transform(df[['Column']])
    df['Transformed Column'] = transformed_column
    # Inverse transformation
    original_column = transformer.inverse_transform(df[['Transformed Column']])
    df['Column'] = original_column

import numpy as np

def numpy_transformation(df):
    
    '''Covers:
        1. Inverse Hyperbolic Sine
        2. Log difference
        3. Penetration Logit
    '''
    
    # Inverse Hyperbolic Sine
    df['Transformed Column'] = np.arcsinh(df['Column'])
    df['Column'] = np.sinh(df['Transformed Column'])
    
    # Log difference
    first_value = df['Column'].iloc[0] #value that will be added to get the first inversed value
    df['Transformed Column'] = np.log(df['Column']).diff()
    df['Column'] = np.exp(df['Transformed Column'].cumsum() + np.log(
        first_value))
    
    # Penetration Logit
    
    # Transforation
    df['Penetration'] = (df['Column']/sum(df['Column'])).clip(1e-6,1 - 1e-6)
    df['Transformed Column'] = np.log(df['Penetration']/(1 - df['Penetration']))
    # Inverse transformation
    df['Inversed Penetration'] = 1/(1 + np.exp(-df['Transformed Column']))
    df['Sum Column'] = [sum(df['Previous Column'])] * len(df) # Previous column is the column before transformation
    df['Column'] = df['Inversed Penetration'] * df['Sum Column']

'''Hypothesis test for stationarity'''
from statsmodels.tsa.stattools import adfuller
from statsmodels.stats.diagnostic import acorr_ljungbox

def hypothesis_test(series):
    
    '''Covers:
            1.Random walk-> Augmented Dickey-Fuller test
            2. White noise -> Ljung-Box test
    '''
    
    '''Input: A series containing the values'''
    
    # Augmented Dickey-Fuller test
    result = adfuller(series)
    print ('ADF Statistics:', result[0])
    print ('p-value:', result[1])
    print ('Critical Values:')
    for key,value in result[4].items():
        print (f'{key}:{value}')
    
    if result[1] > 0.05:
        print ("\nFail to reject the null hypothesis - the time series appears to have a unit root and is non-stationary (random walk).")
    else:
        print ("\nReject the null hypothesis - the time series does not have a unit root and is stationary.")
    
    # Ljung-Box test
    lag = 12
    ljung_box_results = acorr_ljungbox(series, lags = lag, return_df = True)
    print (ljung_box_results)
    
    significant_lags = ljung_box_results[ljung_box_results['lb_pvalue'] < 0.05]
    if significant_lags.empty:
        print ('\nLag:'+str(lag)+" - The time series appears to be white noise (no autocorrelation).")
    else:
        print ('\nLag:'+str(lag)+" - The time series shows signs of autocorrelation and is not white noise.")

    
    
    
    

    


    