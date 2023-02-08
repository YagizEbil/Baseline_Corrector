import numpy as np
import os
import matplotlib.pyplot as plt
from arPLS import arPLS_baseline_correction
from pybaselines import Baseline, utils
from smoothie import moving_average
from process_data import min_max_normalization
from process_data import find_closest_index
from read_data import XYReader
import pandas as pd 
from input_system import MultipleChoiceQuestion
from input_system import FileSelector
from input_system import OpenEndedQuestion

fs = FileSelector("txt,csv,xlsx","doc/")

document = ""

if fs.foundFiles():
    q = MultipleChoiceQuestion("Would you like to open automatically detected files?","",["Pick From Detected Files", "Pick A Custom File"])
    if q.ask().getIndex()==0: document = fs.ask().getValue()

if document=="":
    q = OpenEndedQuestion("Specify a custom file path", "")
    document = q.ask().getValue()

print(f"Opening document {document}")

xyreader = XYReader(document)

for i in xyreader.values:
    x,y,name = i[0], i[1], i[2]
    idx1 = x.index(813.182)
    idx2 = x.index(1000.186)
    x,y = x[idx1:idx2],y[idx1:idx2]
    y_corrected = arPLS_baseline_correction(y)
    baseline_fitter = Baseline(x_data=x)
    bkg = baseline_fitter.poly(y, poly_order=10)[0]

    #plt.plot(x, y, label='Original')
    #plt.plot(x, y_corrected, label='arPLS')
    #plt.plot(x, y-y_corrected, label="arPLS_Corrected")
    #plt.plot(x,bkg,label="mor")
    #plt.plot(x,y-bkg_1,label="mor_Corrected")
    plt.plot(x, min_max_normalization(moving_average(y-bkg, window_size=10)) , label = name.capitalize())
    xyreader.clear()

plt.title(os.path.basename(xyreader.fileHandle.name))
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.legend()
plt.show()
