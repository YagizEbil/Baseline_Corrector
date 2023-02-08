import numpy as np
import os
import matplotlib.pyplot as plt
from arPLS import arPLS_baseline_correction
from pybaselines import Baseline, utils
from smoothie import moving_average
from read_data import XYReader
import pandas as pd 

#document = input("Enter your document path: ")
document = "01022023 ka[itlar.xlsx"
print("\n")

xyreader = XYReader(document)

for i in xyreader.values:
    x,y = i[0], i[1]
    y_corrected = arPLS_baseline_correction(y)
    baseline_fitter = Baseline(x_data=x)
    bkg_1 = baseline_fitter.mor(y, half_window=30)[0]

    #plt.plot(x, y, label='Original')
    #plt.plot(x, y_corrected, label='arPLS')
    #plt.plot(x, y-y_corrected, label="arPLS_Corrected")
    #plt.plot(x,bkg_1,label="mor")
    #plt.plot(x,y-bkg_1,label="mor_Corrected")
    plt.plot(x, moving_average(y-bkg_1, window_size=10) , label ="Corrected")
    xyreader.clear()

plt.title(os.path.basename(xyreader.fileHandle.name))
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.legend()
plt.show()
