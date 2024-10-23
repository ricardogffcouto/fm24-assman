import re

import numpy as np
import pandas as pd


def convert_wage(wage):
    if pd.isna(wage) or wage == 'N/A':
        return np.nan, np.nan

    # Remove all non-numeric characters except for periods and commas
    wage_value_str = re.sub(r'[^\d.,]', '', wage)

    # If the string is empty after removing non-numeric characters, return NaN
    if not wage_value_str:
        return np.nan, np.nan

    # Replace commas with empty string and convert to float
    try:
        wage_value = float(wage_value_str.replace(',', ''))
    except ValueError:
        return np.nan, np.nan

    # Determine the time period and calculate the yearly wage
    if 'p/w' in wage:
        yearly_wage = wage_value * 52
    elif 'p/m' in wage:
        yearly_wage = wage_value * 12
    elif 'p/y' in wage:
        yearly_wage = wage_value
    else:
        yearly_wage = np.nan  # Fallback if format is not recognized

    return wage_value, yearly_wage


def add_wage_value(df):
    df['Wage Value'], df['Yearly Wage'] = zip(*df['Wage'].map(convert_wage))
    return df