# -*- coding: utf-8 -*-
"""
Created on Fri Jun 27 21:54:22 2025

@author: Amlan Ghosh
"""

''' Discrete Prediction Value
    1. Logistic Regression -> statsmodel
    
    Continuous Prediction Value
    1. Regression -> numpy
        1.1. Random Forest Regression -> scikit learn
        1.2. Gradient Boost Regression -> scikit learn
    2. Quantile regression -> statsmodel
'''

import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import GradientBoostingRegressor
import xgboost as xgb
import statsmodels.api as sm

def LogisticRegression(data):
    
    '''1. statsmodel'''
    
    '''Input: a dataframe with X column lists and y column'''
    y,X = data['y'], data['X']
    model = sm.Logit(y,X) # call the model
    result = model.fit() # fit the model
    
    beta = result.params # coefficient of variabls
    aor = np.exp(beta) # Adjusted Odds Ratio
    conf = result.conf_int() # Confidence Interval
    conf.columns = ['Lower CI','Upper CI'] # Confidence interval columns
    p_values = result.pvalues # p-values
    

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
    
    # XGBoost Regression
    model = xgb.XGBRegressor(
        objective = 'reg:squarederror',
        n_estimators = 100,
        learning_rate = 0.1,
        max_depth = 3,
        random_state = 42
        )
    
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