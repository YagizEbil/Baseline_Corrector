import pandas as pd
import csv

class XYReader:
    values, x_values, y_values, file, fileHandle = [], [], [], "", ""
    
    def __init__(self, filePath):
        self.file = filePath
        self.fileHandle = open(self.file, 'r')
        file_type = filePath.split(".")[-1]
        
        data = getattr(self, 'read_' + file_type, lambda: "err")()
        if data == "err": raise ValueError(
            f"File type {file_type} not supported. Please provide a CSV, txt, or xlsx file.")

    def clear(self):
         self.x_values.clear()
         self.y_values.clear()

    def read_csv(self):
            for row in csv.reader(self.fileHandle):
                self.x_values.append(float(row[0]))
                self.y_values.append(float(row[1]))
            self.values.append((self.x_values.copy(), self.y_values.copy(), "Data"))
            self.clear()
    
    def read_txt(self):
            for line in self.fileHandle.readlines()[1:]:
                values = line.split(" ")
                self.x_values.append(float(values[0]))
                self.y_values.append(float(values[1][:values[1].find("\n")]))
            self.values.append((self.x_values.copy(), self.y_values.copy(), "Data"))
            self.clear()

    def read_xlsx(self):
        xl = pd.ExcelFile(self.file)
        for sheet_name in xl.sheet_names:
            var = pd.read_excel(xl, sheet_name)
            for x in var.iloc[:, 0]:
                self.x_values.append(x)
            for y in var.iloc[:, 1]:
                self.y_values.append(y)
            self.values.append((self.x_values.copy(), self.y_values.copy(), sheet_name))
            self.clear()