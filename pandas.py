# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 01:38:57 2021
@author: Amlan Ghosh
"""
import pandas as pd

class Pandas:
    
    def __init__(self, dataframe, value, value1, iterator, excel, csv):
        self.dataframe = dataframe
        self.value = value
        self.value1 = value1
        self.iterator = iterator
        self.excel = excel
        self.csv = csv
        
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
    
    ''' 4) Reading from file'''
    def reading(self):
        if excel_data:
            return self.pd.read_excel(self.excel, sheet_name = None)
        elif csv_data:
            return self.pd.read_csv(self.csv, delimeter = ',')
    
    '''5) Reading row by row of a dataframe'''
    def read_rowbyrow(self):
        for row in self.dataframe.itertuples(): #whole row is a tuple, values are obtained from using tuple index, first element is dataframe index
            continue
    
    ''' 6) Filtering dataframe based on multiple values of a column '''
    def filter_data(self):
        return self.dataframe[(self.dataframe['Column1'] == self.value) | (self.dataframe['Column1'] == self.value1)] # | is representing OR
    
    ''' 7) Replacing some values in a column '''
    self.dataframe['Column1'].replace({'value1': 'value2'}, inplace = True)

