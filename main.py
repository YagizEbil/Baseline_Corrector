from arPLS import arPLS_baseline_correction
from pybaselines import Baseline, utils
from smoothie import moving_average

document = input("Enter your document path: ")
print("\n")
document_type = document[-3:]
documentflag = False

if document_type == "lsx":
  import pandas as pd
  import matplotlib.pyplot as plt

  x_values = []
  y_values = []

  var = pd.read_excel(document)
  for x in var.iloc[:, 0]:
    x_values.append(float(x))
  for y in var.iloc[:, 1]:
    y_values.append(float(y)) 

  documentflag = True

elif document_type == "txt":
  database = []
  x_values = []
  y_values = []

  data = open(document,"r")
  for line in data:
    database.append(line)
  database.pop(0)

  for line in database:
    values = line.split(" ")
    x_values.append(float(values[0]))
    y_values.append(float(values[1][:values[1].find("\n")]))

  documentflag = True

elif document_type == "CSV":
  import csv

  x_values = []
  y_values = []

  with open(document, 'r') as file:
    csvreader = csv.reader(file)
    for row in csvreader:
      x_values.append(float(row[0]))
      y_values.append(float(row[1]))

  documentflag = True

else:
  print("Document type unavaliable")

if documentflag:
  import matplotlib.pyplot as plt
  import numpy as np
      
  y = y_values
  x = x_values

  y_corrected = arPLS_baseline_correction(y)
  baseline_fitter = Baseline(x_data=x)
  bkg_1 = baseline_fitter.mor(y, half_window=30)[0]

  plt.plot(x, y, label='Original')
  #plt.plot(x, y_corrected, label='arPLS')
  #plt.plot(x, y-y_corrected, label="arPLS_Corrected")
  plt.plot(x,bkg_1,label="mor")
  plt.plot(x,y-bkg_1,label="mor_Corrected")
  plt.plot(x, moving_average(y-bkg_1, window_size=10) , label ="smother")
  
  plt.title("Baseline_Correction")
  plt.xlabel("X Axis")
  plt.ylabel("Y Axis")
  plt.legend()
  plt.show()