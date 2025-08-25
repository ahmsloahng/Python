# -*- coding: utf-8 -*-
"""
Created on Fri May  7 21:39:05 2021

@author: Amlan Ghosh
"""

import os
file = 'file location'
os.startfile(file)

folder = 'folder'
subfolder = 'subfolder'

# join folder and file path, any number of inputs
path = os.path.join(folder,subfolder,file)

# get all the files from a folder
file_list = [f for f in os.listdir(folder)]