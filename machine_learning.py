# -*- coding: utf-8 -*-
"""
Created on Fri Jun 27 21:54:22 2025

@author: Amlan Ghosh
"""

'''Continuous Prediction Value
    1. Regression
'''

import numpy as np

def numpy_regression(data):
    '''Input: a dataframe with x column and y column'''
    slope, intercept = np.ployfit(data['y'], data['x'])