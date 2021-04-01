# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 01:38:57 2021

@author: Amlan Ghosh
"""
import pandas as pd

class Pandas:
    
    def __init__(self, dataframe, value, iterator, excel):
        self.dataframe = dataframe
        self.value = value
        self.iterator = iterator
        self.excel = excel
        
    ''' 1) Filtering subset of dataframe with respect to values in a column'''
    def subdataframe_singlevalue(self):
        return self.dataframe[self.dataframe['Value'] == self.value]
    
    def subdataframe_multiplevalues(self):
        return self.dataframe[self.dataframe['Value'].isin(self.iterator)]

    ''' 2) Checking if dataframe is empty'''
    def check_if_empty_df(self):
        return self.dataframe.empty #Returns Boolean value   
    
    ''' 3) Creating dictionary from dataframe with two columns'''
    def create_dictionary(self):
        return self.dataframe.groupby(['Column1']).sum().to_dict['Column2'] #sums all the values corresponding to the values in Column1
    
    ''' 4) Reading from excel file and sheet'''
    def excel_reading(self):
        return self.pd.read_excel(self.excel, sheet_name = None)