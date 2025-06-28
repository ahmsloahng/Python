# -*- coding: utf-8 -*-
"""
Created on Sat Jun 28 18:49:54 2025

@author: Amlan Ghosh
"""
import pandas as pd

'''Granger causality test'''
from statsmodels.tsa.stattools import grangercausalitytests

df = pd.DataFrame({'Target Column':[],'Cause Column':[]})
max_lags = 8
test_result = grangercausalitytests(df, max_lags, verbose = True)
