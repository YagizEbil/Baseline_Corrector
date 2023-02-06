import pandas as pd
import csv

class XYReader:
    x_values, y_values, file = [], [], ""
    
    def __init__(self, filePath):
        self.file = filePath
        file_type = filePath.split(".")[-1]
        
        data = getattr(self, 'read_' + file_type, lambda: "err")()
        if data == "err": raise ValueError(
            f"File type {file_type} not supported. Please provide a CSV, txt, or xlsx file.")

    def read_csv(self):
        with open(self.file, 'r') as data:
            for row in csv.reader(data):
                self.x_values.append(float(row[0]))
                self.y_values.append(float(row[1]))
    
    def read_txt(self):
        with open(self.file, "r") as data:
            for line in data.readlines()[1:]:
                values = line.split(" ")
                self.x_values.append(float(values[0]))
                self.y_values.append(float(values[1][:values[1].find("\n")]))

    def read_xlsx(self):
        var = pd.read_excel(self.file, 0)
        for x in var.iloc[:, 0]:
            self.x_values.append(x)
        for y in var.iloc[:, 1]:
            self.y_values.append(y)