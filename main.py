import numpy as np
import os
import matplotlib.pyplot as plt
from arPLS import arPLS_baseline_correction
from pybaselines import Baseline, utils
from smoothie import moving_average
from normalizer import min_max_normalization
from read_data import XYReader
import pandas as pd 

document = input("Enter your document path: ")
print("\n")

xyreader = XYReader(document)

for i in xyreader.values:
    x,y,name = i[0], i[1], i[2]
    idx1 = x.index(813.182)
    idx2 = x.index(1000.186)
    x,y = x[idx1:idx2],y[idx1:idx2]
    y_corrected = arPLS_baseline_correction(y)
    baseline_fitter = Baseline(x_data=x)
    bkg_1 = baseline_fitter.mor(y, half_window=30)[0]

    #plt.plot(x, y, label='Original')
    #plt.plot(x, y_corrected, label='arPLS')
    #plt.plot(x, y-y_corrected, label="arPLS_Corrected")
    #plt.plot(x,bkg_1,label="mor")
    #plt.plot(x,y-bkg_1,label="mor_Corrected")
    plt.plot(x, min_max_normalization(moving_average(y-bkg_1, window_size=10)) , label = name.capitalize())
    xyreader.clear()

plt.title(os.path.basename(xyreader.fileHandle.name))
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.legend()
plt.show()
