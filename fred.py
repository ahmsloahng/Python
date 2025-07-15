# -*- coding: utf-8 -*-
"""
Created on Tue Jul 15 11:37:04 2025

@author: Amlan Ghosh
"""

import requests
import pandas as pd

# FRED API key
api_key = 'key' # Create an account fredaccount.stlouisfed.org/apikey

#  The URL for FRED series
endpoint = 'https://api.stlouisfed.org/fred/series/observations'

# Parameters for the API call

'''Series:
    1. CPI: CPIAUCSL
    2. Consumer Sentiment: UMCSENT
    3. GDP Growth: A191RL1Q225SBEA
    4. Average Gas Price: GASALLW
    5. Mortage Rate: MORTGAGE30US
    6. Vehicle Loan Rate: RIFLPBCIANM72NM
'''

params = {
    'series_id':'Series',
    'api_key':api_key,
    'file_type':'json'
    }

# Make the API request
response = requests.get(endpoint, params = params)

# Check if requet is successful and convrt to df

if response.status_code == 200:
    data = response.json()
    observations = data.get('observations',[])
    
    # Convert to DataFrame
    df = pd.DataFrame(observations)
    print (df.head())
else:
    print(f'Error: {response.status_code} - {response.text}')