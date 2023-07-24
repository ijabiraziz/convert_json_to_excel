import os
import pandas as pd


from utils import load_json, extract_desired_columns


def json_to_excel(json_file, output_file):
    # Load JSON data with 'utf-8' encoding
    data = load_json(json_file)

    # Extract specific columns
    desired_columns = extract_desired_columns()
    df = pd.json_normalize(data)[desired_columns]

    # Rename the columns
    column_names = {'_id.$oid': 'recipe_id', 'name': 'name', 'nutritional_contents.protein': 'protein',
                    'nutritional_contents.carbohydrates': 'carbs', 'nutritional_contents.fat': 'fats', 'nutritional_contents.energy.unit': 'unit'}
    df = df.rename(columns=column_names)

    # Write the DataFrame to an Excel file
    df.to_excel(output_file, index=False, engine='openpyxl')


if __name__ == "__main__":
    # GET CURRENT DIRECTORY (Adjust file path accordingly)
    current_directory = os.getcwd()
    json_files = [file for file in os.listdir(
        current_directory) if file.endswith('.json')]

    for json_file in json_files:
        excel_output = os.path.splitext(json_file)[0] + ".xlsx"
        json_to_excel(json_file, excel_output)
