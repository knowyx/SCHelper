import json


def read():
    with open('resources/timetable.json', 'r', encoding='utf-8-sig') as file:
        timetable = json.load(file)
    return timetable


def write(data):
    with open('resources/timetable.json', 'w', encoding='utf-8-sig') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
    