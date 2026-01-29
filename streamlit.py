# -*- coding: utf-8 -*-
"""
Created on Thu Jan 29 08:06:16 2026

@author: Amlan Ghosh
"""

import streamlit as st

'''Radio Button'''
options = ['option1','option2','option3']
selected_option = st.radio('Select option:', options, horizontal = True)