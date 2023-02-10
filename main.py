import os
import matplotlib.pyplot as plt
import logging 
from arPLS import arPLS_baseline_correction
from pybaselines import Baseline
from read_data import XYReader
from settings import Settings
from process_data import moving_average, min_max_normalization, find_closest_index, wavenumber_converter
from input_system import MultipleChoiceQuestion, FileSelector, OpenEndedQuestion

logging.basicConfig(level=logging.INFO,format='[BaselineCorrector] [%(levelname)s]: %(message)s')
settings = Settings()
fs = FileSelector("txt,csv,xlsx","doc/")

def show_main_menu():
    mainMenu = MultipleChoiceQuestion("====Baseline Corrector====","",[])
    detectedFileOption = "Pick From Detected Files"
    customFileOption = "Pick A Custom File"
    settingsOption = "Change Settings"

    if fs.foundFiles(): mainMenu.addOption(detectedFileOption)
    mainMenu.addOption(customFileOption)
    mainMenu.addOption(settingsOption)
    document=""
    while(True):
        mainResponse = mainMenu.ask().getValue()
        if mainResponse == detectedFileOption:
            document = fs.ask().getValue()
            break
        elif mainResponse == customFileOption:
            customFileQuestion = OpenEndedQuestion("Specify a custom file path", "")
            document = customFileQuestion.ask().getValue()

            if os.path.isfile(document): break
            else:
                logging.error(f"File ({document}) does not exist")

        elif mainResponse == settingsOption:
            settings.showSettingsMenu()
    plot_document(document)
    settings.save()

def plot_document(document):
        
    logging.info(f"Opening \"{document}\"")

    xyreader = XYReader(document)

    for i in xyreader.values:
        x,y,name = wavenumber_converter(i[0]), i[1], i[2]

        if settings.getSetting("threshold_enabled") == "True": #bool(settings.getSetting("threshold_enabled")):
            dataStartIndex = find_closest_index(float(settings.getSetting("threshold_cutoff_start")), x)
            dataEndIndex = find_closest_index(float(settings.getSetting("threshold_cutoff_end")), x)

            if dataStartIndex!=dataEndIndex:
                x,y = x[dataStartIndex:dataEndIndex],y[dataStartIndex:dataEndIndex]
            else:
                logging.error(f"Couldn't apply threshold, showing unaltered graph.")

        y_corrected = arPLS_baseline_correction(y)
        baseline_fitter = Baseline(x_data=x)
        bkg_1 = baseline_fitter.mor(y, half_window=30)[0]

        plt.plot(x, min_max_normalization(moving_average(y-bkg_1, window_size=10)) , label = name.capitalize())
        xyreader.clear()

   # plt.title(os.path.basename(xyreader.fileHandle.name))
    plt.xlabel("Raman Shift Wavenumber (cm-1)")
    plt.ylabel("Intensity (a.u.)")
    plt.legend()
    plt.show()

show_main_menu()