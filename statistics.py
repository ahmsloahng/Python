# -*- coding: utf-8 -*-
"""
Created on Sat Jun 28 18:49:54 2025

@author: Amlan Ghosh
"""
import pandas as pd
from prophet import Prophet
import matlotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import GradientBoostingRegressor

'''Granger causality test'''
from statsmodels.tsa.stattools import grangercausalitytests

df = pd.DataFrame({'Target Column':[],'Cause Column':[]})
max_lags = 8
test_result = grangercausalitytests(df, max_lags, verbose = True)

'''Shap Kernel explainer'''
import shap

'''
1. Prophet
'''

# Input df:-> columns ds,y,exogenous variables
df_train = df.iloc[:80]
df_test = df.iloc[80:]
model = Prophet()
model.fit(df_train)

ds = [df['ds'].iloc[0]]
exog_list = [col for col in df.columns if col not in ['ds','y']]

def prophet_predict(X):
    df_pred = pd.DataFrame(X, columns = exog_list)
    df_pred['ds'] = ds * len(df_pred)
    forecast = model.predict(df_pred)
    return forecast['yhat'].values

X_train_exog = df_train[exog_list].values
explainer = shap.KernelExplainer(prophet_predict, X_train_exog)

X_test_exog = df_test[exog_list].values
shap_values = explainer.shap_values(X_test_exog)

'''
2. Tree Explainer
'''

# Input df:-> Target column and other column for variables
df_train = df.iloc[:-80]
df_test = df.iloc[-80:]

y_train = df_train['y'] # Filtering the target variable
del df_train['y'] # Removing the target variable from training data

# Random Forest regression
model = RandomForestRegressor(n_estimators = 100, random_state = 42)

# Gradient Boost regressor
model = GradientBoostingRegressor(random_state = 42)

model.fit(df_train, y_train)

explainer = shap.TreeExplainer(model)
shap_values = explainer.shap_values(df_test)

fig = plt.figure(figsize = (10,8))

# Prophet
shap.summary_plot(shap_values, X_test_exog)

# Tree explainer
shap.summary_plot(shap_values, df_test)
shap.summary_plot(shap_values, df_test, plot_type = 'bar')

fig.savefig('fig.png', dpi = 300, bbox_inches = 'tight')
plt.close(fig)

idx = 0

instance_shap_values = shap_values[idx]
instance_base_value = explainer.expected_value[idx]

explanation = shap.Explanation(
    values = instance_shap_values,
    base_values = instance_base_value,
    data = df_test.iloc[idx],
    feature_names = df_test.columns.to_list()
    )

shap.plots.waterfall(explanation)