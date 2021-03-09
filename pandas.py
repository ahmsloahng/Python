# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 01:38:57 2021

@author: Amlan Ghosh
"""
class Pandas:
    
    def __init__(self, dataframe, value, iterator):
        self.dataframe = dataframe
        self.value = value
        self.iterator = iterator
        
    ''' 1) Filtering subset of dataframe with respect to values in a column'''
    def subdataframe_singlevalue(self):
        return self.dataframe[self.dataframe['Value'] == self.value]
    
    def subdataframe_multiplevalues(self):
        return self.dataframe[self.dataframe['Value'].isin(self.iterator)]

    ''' 2) Checking if dataframe is empty'''
    def check_if_empty_df(self):
        return self.dataframe.empty #Returns Boolean value   