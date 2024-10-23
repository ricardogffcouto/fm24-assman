import json
import os

FILTERS_FOLDER = 'data/filters'

def save_filter(filter_name, filter_model):
    if not os.path.exists(FILTERS_FOLDER):
        os.makedirs(FILTERS_FOLDER)
    file_path = os.path.join(FILTERS_FOLDER, f"{filter_name}.json")
    with open(file_path, 'w') as f:
        json.dump(filter_model, f)

def load_filter(filter_name):
    file_path = os.path.join(FILTERS_FOLDER, f"{filter_name}.json")
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            return json.load(f)
    return None

def get_saved_filters():
    if not os.path.exists(FILTERS_FOLDER):
        return []
    return [f.split('.')[0] for f in os.listdir(FILTERS_FOLDER) if f.endswith('.json')]