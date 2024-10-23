import pandas as pd
from bs4 import BeautifulSoup
import os

def make_unique(columns):
    seen = set()
    for i, col in enumerate(columns):
        original = col
        counter = 1
        while col in seen:
            col = f"{original}.{counter}"
            counter += 1
        seen.add(col)
        columns[i] = col
    return columns

def read_file(file_name):
    # Check if parquet file exists
    parquet_file = f'data/{file_name}.parquet'
    if os.path.exists(parquet_file):
        print(f"Parquet file {parquet_file} already exists. Reading from it.")
        return pd.read_parquet(parquet_file)

    # If parquet file doesn't exist, read from HTML and create parquet
    print(f"Parquet file not found. Reading from HTML and creating {parquet_file}")
    with open(f'data/{file_name}.html', 'r', encoding='utf-8') as file:
        html_content = file.read()

    # Parse the HTML content
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find the table in the HTML
    table = soup.find('table')

    # Extract table headers
    headers = [th.text.strip() for th in table.find_all('th')]

    # Extract table data
    data = [[td.text.strip() for td in row.find_all('td')] for row in table.find_all('tr')[1:]]

    # Create a pandas DataFrame
    df = pd.DataFrame(data, columns=headers)

    # Rename duplicate columns
    df.columns = make_unique(list(df.columns))

    # Save as parquet file
    df.to_parquet(parquet_file)
    print(f"Parquet file {parquet_file} created.")

    return df

def add_foot_scores(df):
    foot_mapping = {
        'Fairly Strong': 4,
        'Very Strong': 5,
        'Reasonable': 2,
        'Strong': 3,
        'Weak': 1,
        'Very Weak': 0
    }

    df['Left Foot Score'] = df['Left Foot'].map(foot_mapping)
    df['Right Foot Score'] = df['Right Foot'].map(foot_mapping)
    df['Footedness Score'] = df['Left Foot Score'] + df['Right Foot Score']
    return df

def add_extra_attributes(df):
    df = add_foot_scores(df)
    return df

# Example usage
file_name = '2025-01 Youth'
df = read_file(file_name)
df = add_extra_attributes(df)
print(df.head())
print(df.columns)  # Print column names to verify uniqueness
