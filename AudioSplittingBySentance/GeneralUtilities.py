import json


def get_config_file_data(config_file_path):
    with open(config_file_path, "r") as file:
        data = json.load(file)
    return data
