# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 01:38:57 2021
@author: Amlan Ghosh
"""
import pandas as pd
import numpy as np

class Pandas:
    
    def __init__(self, dataframe, value, value1, iterator, excel, csv, data_type):
        self.dataframe = dataframe
        self.value = value
        self.value1 = value1
        self.iterator = iterator
        self.excel = excel
        self.csv = csv
        self.data_type = data_type
        
    ''' 1. Filtering subset of dataframe with respect to values in a column'''
    def subdataframe_singlevalue(self):
        return self.dataframe[self.dataframe['Value'] == self.value]
    
    def subdataframe_multiplevalues(self):
        return self.dataframe[self.dataframe['Value'].isin(self.iterator)]

    ''' 2. Checking if dataframe is empty'''
    def check_if_empty_df(self):
        return self.dataframe.empty #Returns Boolean value   
    
    ''' 3. Creating dictionary from dataframe with two columns'''
    def create_dictionary(self):
        return self.dataframe.groupby(['Column1']).sum().to_dict['Column2'] #sums all the values corresponding to the values in Column1
    
    ''' 4. Reading from file'''
    def reading(self):
        if self.data_type == 'excel':
            return self.pd.read_excel(self.excel, sheet_name = None)
        elif self.data_type == 'csv':
            return self.pd.read_csv(self.csv, delimeter = ',')
    
    '''5. Reading row by row of a dataframe'''
    def read_rowbyrow(self):
        for row in self.dataframe.itertuples(): #whole row is a tuple, values are obtained from using tuple index, first element is dataframe index
            continue
    
    ''' 6. Filtering dataframe based on multiple values of a column '''
    def filter_data(self):
        return self.dataframe[(self.dataframe['Column1'] == self.value) | (self.dataframe['Column1'] == self.value1)] # | is representing OR
    
    ''' 7. Replacing some values in a column '''
    def replace(self):
        return self.dataframe['Column1'].replace({'value1': 'value2'}, inplace = True)
    def replace_on_condition(self):
        mask = self.dataframe['Column1'] == 'value1' # can be >, < also
        self.dataframe.loc[mask,'Column1'] = 'value2'
        return self.dataframe
    
    '''8. Groupby and aggregate'''
    def groupbyagg(self):
        return self.dataframe.groupby('Column1').agg({
            'Column2':'sum',
            'Column3':'mean'}).reset_index()
    
    '''9. Writing in multple sheets of excel'''
    def multiplesheetinexcel(self):
        with pd.ExcelWriter('Excel File.xlsx', engine = 'openpyxl') as writer:
            self.dataframe.to_excel(writer, sheet_name = 'sheet', index = False)

    '''10. Sort the dataframe by a column'''
    def sort(self):
        return self.dataframe.sort_values(by = 'Column1', ascending = True)
    
    '''11. Count the number of occurrence of a value in a column'''
    def count_frequency(self,col,val):
        return (col == val).sum()
    
    '''12. Month on month percentage change'''
    def percentage_change(self):
        self.dataframe['MoM Revenue Growth'] = self.dataframe['Revenue'].pct_change()
        return self.dataframe
    
    '''13. Create a dataframe with NaN values'''
    def create_df_with_nan(self):
        dataframe = pd.DataFrame({'Column1':['value']*10,
                                  'Column2':[np.nan]*10})

'''Dictionary Questions
1. I have a dataframe with a single column having index of anything. I want to convert the 
dataframe to a dictionary where the keys will be the index and the values in column will be 
values of the dictionary. The column name will not be used any where. How to do it?
'''

dic = pd.DataFrame({'Column':[1,2,3,4]}, index = ['row1','row2','row3','row4'])
final_dic = dic['Column'].to_dict()

'''Input: 
      Column
row1       1
row2       2
row3       3
row4       4

Output: {'row1': 1, 'row2': 2, 'row3': 3, 'row4': 4}
'''

'''
2. I have a dataframe having 2 columns. I want to have the dataframe sorted in
such a way that rows containing certain values from column 1 always appear on
top.
Input:
    Column1 Column2
    value1  0
    value2  1
    value3  2
    value4  3
    value5  4
    
Output:
    Column1 Column2
    value3  2
    value5  4
    value1  0
    value2  1
    value4  3
'''

df_2 = pd.DataFrame({'Column1':['value1','value2','value3','value4','value5'],
                    'Column2':[0,1,2,3,4]})

df_2_imp = df_2[df_2['Column1'].isin(['value3','value5'])]
df_2_rem = df_2[~(df_2['Column1'].isin(['value3','value5']))]

df_2 = pd.concat([df_2_imp,df_2_rem], ignore_index = True)

'''Convert a dictionary to dataframe where keys will be on column and values 
will be another'''
dic = None
df = pd.DataFrame(list(dic.items()), columns = ['Column1','Column2'])

