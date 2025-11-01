import csv


def read(file):
    data = []
    with open(file, encoding='UTF-8') as f:
        reader = csv.DictReader(f)
        for x in reader:
            data.append(x)
    return data
