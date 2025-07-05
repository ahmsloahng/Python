# -*- coding: utf-8 -*-
"""
Created on Fri Jun 27 21:54:22 2025

@author: Amlan Ghosh
"""

'''Continuous Prediction Value
    1. Regression -> numpy
    2. Quantile regression -> statsmodel
'''

import numpy as np

def regression(data):
    
    '''1. numpy'''
    
    '''Input: a dataframe with x column and y column'''
    slope, intercept = np.ployfit(data['y'], data['x'])

import statsmodel.formula.api as smf

def quantile_regression(data, future_data):
    
    '''2. statsmodel'''
    
    '''Input: 
        a dataframe with x1,x2 column and y column
        a dataframe contains future dates with column x1 and x2
    '''
    quantile = 0.5 # quantile we need to predict
    formula = 'y ~ x1 + x2' # formula defining the independent variables needed to be considered
    model = smf.quantreg(formula, data) # define the model
    result = model.fit(q = quantile) # fit the model
    future = result.predict(future_data) # predict