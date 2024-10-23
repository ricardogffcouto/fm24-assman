import re

import numpy as np
import pandas as pd


def load_personality_media_handling_data(file_path):
    df = pd.read_csv(file_path, index_col=0)
    df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
    return df

def split_range(value):
    if pd.isna(value) or value == '-' or value == '*':
        return np.nan, np.nan
    parts = str(value).split('-')
    for i in range(len(parts)):
        parts[i] = re.sub(r'[^\d.,]', '', parts[i])
    if len(parts) == 1:
        return float(parts[0]), float(parts[0])
    return float(parts[0]), float(parts[1])
