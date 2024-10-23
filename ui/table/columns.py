import json
import os

FILTERS_FOLDER = 'data/columns'

def save_column(column_name, column_model):
    if not os.path.exists(FILTERS_FOLDER):
        os.makedirs(FILTERS_FOLDER)
    file_path = os.path.join(FILTERS_FOLDER, f"{column_name}.json")
    with open(file_path, 'w') as f:
        json.dump(column_model, f)

def load_column(column_name):
    file_path = os.path.join(FILTERS_FOLDER, f"{column_name}.json")
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            return json.load(f)
    return None

def get_saved_columns():
    if not os.path.exists(FILTERS_FOLDER):
        return []
    return [f.split('.')[0] for f in os.listdir(FILTERS_FOLDER) if f.endswith('.json')]