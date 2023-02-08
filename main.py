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
from settings import Settings

settings = Settings()
fs = FileSelector("txt,csv,xlsx","doc/")

document = ""

mainMenu = MultipleChoiceQuestion("====Baseline Corrector====","",[])
detectedFileOption = "Pick From Detected Files"
customFileOption = "Pick A Custom File"
settingsOption = "Change Settings"

if fs.foundFiles(): mainMenu.addOption(detectedFileOption)
mainMenu.addOption(customFileOption)
mainMenu.addOption(settingsOption)

while(True):
    mainResponse = mainMenu.ask().getValue()
    if mainResponse == detectedFileOption:
        document = fs.ask().getValue()
        break
    elif mainResponse == customFileOption:
        customFileQuestion = OpenEndedQuestion("Specify a custom file path", "")
        document = customFileQuestion.ask().getValue()
        break
    elif mainResponse == settingsOption:
        settings.showSettingsMenu()
    
print(f"Opening document {document}")

xyreader = XYReader(document)

for i in xyreader.values:
    x,y,name = i[0], i[1], i[2]
    dataStartIndex = find_closest_index(float(settings.getSetting("threshold_cutoff_start")), x)
    dataEndIndex = find_closest_index(float(settings.getSetting("threshold_cutoff_end")), x)

    if dataStartIndex!=dataEndIndex:
        x,y = x[dataStartIndex:dataEndIndex],y[dataStartIndex:dataEndIndex]
    else:
        print(f"Error! Couldn't apply threshold, showing unaltered graph.")

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
