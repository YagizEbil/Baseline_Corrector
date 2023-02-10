import json
from input_system import OpenEndedQuestion
from input_system import MultipleChoiceQuestion
import logging

class Settings:

    jsonFilename = "baseline-settings.json"
    settingDictionary = {}

    def __init__(self):
        self.load()
        self.defaults()
    
 #   def __del__(self):
  #      self.save()
    
    def defaults(self):
        self.addDefault("threshold_cutoff_start",0)
        self.addDefault("threshold_cutoff_end",2500)
        self.addDefault("threshold_enabled", False)

    def showSettingsMenu(self):
        while(True):
            q = MultipleChoiceQuestion("Settings: ", "Select a setting to change or continue",[])
            q.addOption("Continue")
            q.addOption("Reset to defaults")

            for k,v in self.settingDictionary.items():
                q.addOption(f"{k} = {v}")

            index = q.ask().getIndex()-2
            if index==-2: break
            if index==-1:
                self.settingDictionary.clear()
                self.defaults()
                continue

            settingKey = list(self.settingDictionary.keys())[index]

            qs = OpenEndedQuestion(f"Change Setting: \"{settingKey}\" -> ?", f"Current value = {self.settingDictionary[settingKey]}")
            newVal = qs.ask().getValue()

            self.setSetting(settingKey, newVal)
        self.save()

    def setSetting(self, key, val):
        self.settingDictionary[key] = val

    def getSetting(self, key):
        if key not in self.settingDictionary:
            return ""
        return self.settingDictionary[key]

    def addDefault(self, key, defaultValue):
        if key not in self.settingDictionary:
            self.settingDictionary[key] = defaultValue

    def load(self):
        try:
            with open(self.jsonFilename, 'r') as openfile:
                self.settingDictionary = json.load(openfile)
        except IOError:
            pass

    def save(self):
        jsonObject = json.dumps(self.settingDictionary, sort_keys=True, indent=4)
        with open(self.jsonFilename, "w") as outfile:
            outfile.write(jsonObject)
        logging.info("Saved settings.")
