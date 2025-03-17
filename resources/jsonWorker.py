import json


def read(file):
    with open(file, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def write(file, data):
    with open(file, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def writeAdd(file, newLine):
    data = read(file)
    data.append(newLine)
    write(file, data)


def elementDeletion(file, elementIndex):
    data = read(file)
    
    if 1 <= elementIndex <= len(data):
        del data[elementIndex - 1]
        write(file, data)
    else:
        print(f"Ошибка: Индекс {elementIndex} вне диапазона [1, {len(data)}]")
