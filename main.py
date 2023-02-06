import numpy as np
import matplotlib.pyplot as plt
from arPLS import arPLS_baseline_correction
from pybaselines import Baseline, utils
from smoothie import moving_average
from read_data import XYReader

document = input("Enter your document path: ")
print("\n")

xyreader = XYReader(document)
x, y = xyreader.x_values, xyreader.y_values

y_corrected = arPLS_baseline_correction(y)
baseline_fitter = Baseline(x_data=x)
bkg_1 = baseline_fitter.mor(y, half_window=30)[0]

plt.plot(x, y, label='Original')
# plt.plot(x, y_corrected, label='arPLS')
# plt.plot(x, y-y_corrected, label="arPLS_Corrected")
plt.plot(x, bkg_1, label="mor")
plt.plot(x, y-bkg_1, label="mor_Corrected")
plt.plot(x, moving_average(y-bkg_1, window_size=10), label="smother")

plt.title("Baseline_Correction")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.legend()
plt.show()
