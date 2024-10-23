import numpy as np
import pandas as pd

from processors.utils import split_range, load_personality_media_handling_data


def add_personality_attributes(df):
    personality_df = load_personality_media_handling_data('FM HA Calculator - Personality.csv')

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

def adjust_attributes_based_on_mhs(df):
    mhs_df = load_personality_media_handling_data('FM HA Calculator - Media Handling Style.csv')

    attributes = ['Professionalism', 'Determination', 'Ambition', 'Loyalty', 'Sportsmanship',
                  'Pressure', 'Temperament', 'Leadership', 'Controversy']

    for index, row in df.iterrows():
        mhs = row['Media Handling']
        if mhs in mhs_df.index:
            mhs_data = mhs_df.loc[mhs]

            for attr in attributes:
                min_col, max_col = f'{attr}_min', f'{attr}_max'
                mhs_min, mhs_max = split_range(mhs_data[attr])

                if not pd.isna(mhs_min):
                    df.at[index, min_col] = max(df.at[index, min_col], mhs_min)
                if not pd.isna(mhs_max):
                    df.at[index, max_col] = min(df.at[index, max_col], mhs_max)

            # Handle cases
            cases = str(mhs_data['Cases']).split(',')
            for case in cases:
                if case == '1':
                    df.at[index, 'Professionalism_max'] = min(df.at[index, 'Professionalism_max'], 14)
                    df.at[index, 'Pressure_max'] = min(df.at[index, 'Pressure_max'], 14)
                elif case == '2':
                    df.at[index, 'Loyalty_max'] = min(df.at[index, 'Loyalty_max'], 10)
                    if df.at[index, 'Professionalism_max'] <= 12 and df.at[index, 'Sportsmanship_max'] <= 11:
                        df.at[index, 'Professionalism_max'] = min(df.at[index, 'Professionalism_max'], 12)
                        df.at[index, 'Sportsmanship_max'] = min(df.at[index, 'Sportsmanship_max'], 11)
                elif case == '3':
                    df.at[index, 'Temperament_min'] = max(df.at[index, 'Temperament_min'], 8)
                    df.at[index, 'Sportsmanship_min'] = max(df.at[index, 'Sportsmanship_min'], 8)
                elif case == '4':
                    df.at[index, 'Temperament_max'] = min(df.at[index, 'Temperament_max'], 14)
                    df.at[index, 'Pressure_max'] = min(df.at[index, 'Pressure_max'], 14)
                elif case == '5':
                    df.at[index, 'Controversy_min'] = max(df.at[index, 'Controversy_min'], 6)
                    df.at[index, 'Professionalism_max'] = min(df.at[index, 'Professionalism_max'], 14)
                elif case == '6':
                    df.at[index, 'Professionalism_min'] = max(df.at[index, 'Professionalism_min'], 13)
                    df.at[index, 'Sportsmanship_min'] = max(df.at[index, 'Sportsmanship_min'], 12)

    return df

def add_hidden_attributes(df):
    df = add_personality_attributes(df)
    df = adjust_attributes_based_on_mhs(df)
    return df