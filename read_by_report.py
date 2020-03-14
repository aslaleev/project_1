import csv


def vivod_dannih():
    with open('directory_of_report.csv', 'r' , encoding='utf-8') as ff:
        value = []
        reader = csv.DictReader(ff)
        for line in reader:
            value.append(line)
        return value



