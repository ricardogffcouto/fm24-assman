import re

import numpy as np
import pandas as pd


def load_personality_data(file_path):
    personality_df = pd.read_csv(file_path, index_col=0)
    personality_df = personality_df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
    return personality_df

def split_range(value):
    if pd.isna(value) or value == '-' or value == '*':
        return np.nan, np.nan
    parts = str(value).split('-')
    for i in range(len(parts)):
        parts[i] = re.sub(r'[^\d.,]', '', parts[i])
    if len(parts) == 1:
        return float(parts[0]), float(parts[0])
    return float(parts[0]), float(parts[1])

def add_personality_attributes(df):
    personality_df = load_personality_data('FM HA Calculator - Personality.csv')

    for column in personality_df.columns:
        if column != 'Notes' and column != 'Personalities that have priority over it':
            df[f'{column}_min'] = np.nan
            df[f'{column}_max'] = np.nan

    for index, row in df.iterrows():
        personality = row['Personality']
        if personality in personality_df.index:
            for column in personality_df.columns:
                if column != 'Notes' and column != 'Personalities that have priority over it':
                    value = personality_df.loc[personality, column]
                    min_val, max_val = split_range(value)
                    df.at[index, f'{column}_min'] = min_val
                    df.at[index, f'{column}_max'] = max_val

    return df