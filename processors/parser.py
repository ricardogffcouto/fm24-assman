import pandas as pd
from bs4 import BeautifulSoup
import os

from processors.constants import NUMERIC_COLUMNS
from processors.foot import add_foot_scores
from processors.hidden import add_hidden_attributes
from processors.position import parse_positions
from processors.wage import add_wage_value


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

def add_extra_attributes(df):
    df = add_foot_scores(df)
    df = add_wage_value(df)
    df = add_hidden_attributes(df)
    df = parse_positions(df)
    return df


def convert_columns_to_numeric(df):
    # Convert the specified columns to numeric
    df[NUMERIC_COLUMNS] = df[NUMERIC_COLUMNS].apply(pd.to_numeric, errors='coerce')

    return df


def read_file(file_name):
    # Check if parquet file exists
    parquet_file = f'data/{file_name}.parquet'
    if os.path.exists(parquet_file):
        print(f"Parquet file {parquet_file} already exists. Reading from it.")
        df = pd.read_parquet(parquet_file)
    else:
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

    df = add_extra_attributes(df)

    df = convert_columns_to_numeric(df)

    return df

if __name__ == "__main__":
    df = read_file('2025-01 Youth')
    columns = df.columns
    df.head()
