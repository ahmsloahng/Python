# -*- coding: utf-8 -*-
"""
Created on Fri Jun 27 21:54:22 2025

@author: Amlan Ghosh
"""

'''Continuous Prediction Value
    1. Regression -> numpy
        1.1. Random Forest Regression -> scikit learn
        1.2. Gradient Boost Regression -> scikit learn
    2. Quantile regression -> statsmodel
'''

import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import GradientBoostingRegressor

def regression(data):
    
    '''1. numpy'''
    
    '''Input: a dataframe with x column and y column'''
    slope, intercept = np.ployfit(data['y'], data['x'])
    
    '''2. scikit-learn'''
    
    '''Input: a dataframe with y column and other independent variables'''
    
    train_data = data.iloc[:-80]
    test_data = data.iloc[-80:]
    
    y_train = train_data['y'] # Filtering out the target column
    del train_data['y'] # Deleting target column from training data
    del test_data['y']
    
    # Random Forest Regression
    model = RandomForestRegressor(n_estimator = 100, random_state = 42)
    
    # Gradient Boost Regression
    model = GradientBoostingRegressor(random_state = 42)
    
    model.fit(train_data, y_train) # Train the data
    model.predict(test_data) # Predict
    
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