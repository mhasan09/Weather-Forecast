import json


def process_area_data():
    json_file_path = 'dataset/area.json'
    file = open(json_file_path, encoding="utf8")
    return json.load(file)
