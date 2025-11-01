import csv


def read(file):
    data = []
    with open(file) as f:
        reader = csv.DictReader(f)
        for x in reader:
            data.append(x)
    return data
