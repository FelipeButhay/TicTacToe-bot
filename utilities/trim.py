import csv
import os

direc = os.path.dirname(os.path.abspath(__file__)).replace('\'', '/')
with open(f"{direc}/data.csv", "r") as data:
    csv_reader = csv.reader(data)
    for x in csv_reader:
        if x[3] == "3":
            with open(f"{direc}/newdata.csv", "a") as file:
                csv.writer(file).writerow(x)
    