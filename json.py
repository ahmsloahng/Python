# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 20:26:13 2021

@author: ORMAE
"""

import json

#Reading from json file
with open('file_name.json', 'r') as file_name:
    data = json.load(file_name)
    
#Writing to json file
with open('file_name.json', 'w') as f:
    json.dumo(data, f, indent = 4)
    