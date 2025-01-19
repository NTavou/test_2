"""
# My first app
Here's our first attempt at using data to create a table:
"""

import streamlit as st
import pandas as pd

# Import the Excel file
data = pd.read_excel('01_Todays_Matches_final.xlsx')

# Display the date of the bet forecasts
day = data.iloc[0,0]
month = data.iloc[0,1]
year = data.iloc[0,2]


title = f'Bets for {day}-{month}-{year}:'

title

data





