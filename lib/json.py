import json
import os

current_file_path = os.path.abspath(__file__)
current_directory = os.path.dirname(current_file_path)


def save_to_json_file(filename, data):
    with open(os.path.join(current_directory, "..", "data", f"{filename}.json"), 'w') as f:
        json.dump(data, f, indent=4)


def read_from_json_file(filename):
    with open(os.path.join(current_directory, "..", "data", f"{filename}.json"), 'r') as f:
        data = json.load(f)
    return data
