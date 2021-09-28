# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 01:28:57 2021
@author: Amlan Ghosh
"""
import pandas as pd

'''Define a dictionary with column names as key and empty list for values'''

output_dict = {
                 'Column1': [],
                 'Column2': []
              }

'''Append the values in the list'''
for values in iterator:
    output_dict['Column1'].append(values)
    output_dict['Column2'].append(values)

temp_data = {
            'Column1': output_dict['Column1'],
            'Column2': output_dict['Column2']
            }

df = pd.DataFrame(temp_data, colums = ['Column1', 'Column2'])

df.to_csv(path, index = False)
df.to_excel(path, sheet_name = 'Sheet Name', index = False)

''' multiple sheets in a single excel file '''
with pd.ExcelWriter(path) as writer:
    df.to_excel(writer, sheet_name= 'sheet', index = False)
    df1.to_excel(writer, sheet_name = 'sheet_1', index = False)

