# -*- coding: utf-8 -*-
# импорт модуля работы с файлом
import csv


def read(file):
    # функция чтения из файла
    data = []
    with open(file, encoding='UTF-8') as f:
        reader = csv.DictReader(f)
        for x in reader:
            data.append(x)
    return data
