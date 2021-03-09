# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 23:59:10 2021

@author: Amlan Ghosh
"""
import csv

class CSV:
    
    def __init__(self, inputdata_path, outputdata_path):
        self.inputdata_path = inputdata_path
        self.outputdata_path = outputdata_path
    
    'Reading a csv file'    
    def read_csv(self):
        with open(self.inputdata_path, 'r') as file:
            reader = csv.reader(file)
            next(reader) #To skip the headers if any
            for row in reader:    #row is a list, we can take the values using the indexes
                continue      
    
    'Updating the csv file'
    def update_csv(self):
        with open(self.outputdata_path, 'w', newline = '') as write_file: #newline is given to ensure no spacing in rows while opening csv file in excel
            with open(self.inputdata_path, 'r') as read_file:
                reader = csv.reader(read_file)
                writer = csv.writer(write_file)
                for row in reader:
                    row.append('Joy Mohun Bagan')
                    writer.writerow(row)
                return writer