"""
# My first app
Here's our first attempt at using data to create a table:
"""

import streamlit as st
import pandas as pd
from datetime import datetime


# Specify the file path
file_path = r'C:\\Users\\nikos\\basketball_forecasting-master\\2024_2025\\01_Todays_Matches.xlsx'  # Update this path to match your file's location

# Import the Excel file
data = pd.read_excel(file_path)

# Display the date of the bet forecasts
day = data.iloc[0,1]
month = data.iloc[0,2]
year = data.iloc[0,3]


title = f'Bets for {day}-{month}-{year}:'

title

# Display the first few rows of the dataframe
data.iloc[:, [1, 2, 3, 4, 5,  6, 8, 9]]