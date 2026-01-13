# -*- coding: utf-8 -*-
"""
Created on Tue Aug 26 06:53:33 2025

@author: Amlan Ghosh
"""

# raise value error
k = 10
if k == 10:
    print ('No error')
else:
    raise ValueError('Error')
    
# sort dictionary
def sort_dictionary(dic):
    sorted_items = sorted(dic.items(), key = lambda x:x[1])
    sorted_dic = {k:v for k,v in sorted_items}
    return sorted_dic

'''If any item from list1 is present in list2 then true and enter the loop'''
list1 = None
list2 = None
if any (term in list2 for term in list1):
    condition = True

'''If all term from list1 is present in list2 then true and enter the loop'''
if all (term in list2 for term in list1):
    condition = True
    
'''Pipeline Quality Index'''

df_final = None

import numpy as np
from scipy.stats import rankdata
def percentile(series):
    return rankdata(series, method='average') / len(series)

df_final['op_size_mean_p'] = percentile(np.log1p(df_final['col_opval']))
df_final['op_size_median_p'] = percentile(np.log1p(df_final['col_medianopval']))

df_final['win_pct_p'] = percentile(df_final['col_percwon'])
df_final['won_log_p'] = percentile(np.log1p(df_final['col_snumwon']))

df_final['median_inv_p'] = 1 - percentile(df_final['col_nummediandays'])
df_final['avg_inv_p'] = 1 - percentile(df_final['col_nummeandays'])

df_final['tail_gap_inv_p'] = 1 - percentile(df_final['tail_gap'])
df_final['tail_ratio_inv_p'] = 1 - percentile(df_final['tail_ratio'])

df_final['renewal_p'] = percentile(df_final['col_snumren'])


df_final['win_score'] = (
    0.7 * df_final['win_pct_p'] +
    0.3 * df_final['won_log_p']
)

df_final['velocity_score'] = (
    0.6 * df_final['median_inv_p'] +
    0.4 * df_final['avg_inv_p']
)

df_final['stability_score'] = df_final['renewal_p']

df_final['quality_score'] = (
    0.6 * df_final['op_size_median_p'] +
    0.4 * df_final['op_size_mean_p']
)

df_final['PQI'] = 100 * (
    0.30 * df_final['win_score']
    + 0.25 * df_final['quality_score']
    + 0.25 * df_final['velocity_score']
    + 0.20 * df_final['stability_score']
)
