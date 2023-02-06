import pandas as pd
import csv

def read_data(file):
    file_type = file.split(".")[-1]
    if file_type == "csv":
        x_values = []
        y_values = []

        with open(file, 'r') as file:
            csvreader = csv.reader(file)
            for row in csv.reader(file):
                x_values.append(float(row[0]))
                y_values.append(float(row[1]))

    elif file_type == "txt":
        database = []
        x_values = []
        y_values = []

        data = open(file,"r")
        for line in data:
            database.append(line)
            database.pop(0)

        for line in database:
            values = line.split(" ")
            x_values.append(float(values[0]))
            y_values.append(float(values[1][:values[1].find("\n")]))

    elif file_type == "xlsx":
        x_values = []
        y_values = []

        var = pd.read_excel(file, 0)
        for x in var.iloc[:, 0]:
            x_values.append(x)
        for y in var.iloc[:, 1]:
            y_values.append(y) 

    else:
        raise ValueError("File type not supported. Please provide a CSV, txt, or xlsx file.")

