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