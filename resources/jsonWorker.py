import json


def read(file):
    with open(file, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def write(file, data):
    with open('resources/timetable.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)