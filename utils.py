import json


def load_json(json_file):
    with open(json_file, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def extract_desired_columns():
    desired_columns = ['_id.$oid', 'name', 'nutritional_contents.protein',
                       'nutritional_contents.carbohydrates', 'nutritional_contents.fat', 'nutritional_contents.energy.unit']

    return desired_columns
