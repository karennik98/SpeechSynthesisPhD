import json


def get_config_file_data(config_file_path):
    with open(config_file_path, "r") as file:
        data = json.load(file)
    return data


def save_json_data(data, file_path):
    with open(file_path, 'w') as json_file:
        json.dump(data, json_file, indent=2)