import pybaselines
from pybaselines import Baseline, utils
from read_data import XYReader
import matplotlib.pyplot as plt
from smoothie import moving_average
from process_data import min_max_normalization
import os 

document = "doc\Boş_Metal.xlsx"
xyreader = XYReader(document)

for i in xyreader.values:
    x,y,name = i[0], i[1], i[2]
    baseline_fitter = Baseline(x_data=x)

    bkg = baseline_fitter.quant_reg(y ,2,0.05,0.000001,250)

    plt.plot(x, y, label='Original') 
    plt.plot(x, moving_average(y, window_size=10) , label = name.capitalize())

plt.title(os.path.basename(xyreader.fileHandle.name))
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.legend()
plt.show()
