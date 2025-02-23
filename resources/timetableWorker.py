import json

def read():
    with open('resources/timetable.json', 'r', encoding='utf-8-sig') as file:
        timetable = json.load(file)
    return timetable

read()