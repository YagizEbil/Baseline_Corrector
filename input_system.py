class FileSelector:

    files = []
    question = 0

    def __init__(self, supportedTypes, path):
        import glob
        self.suportedTypes = supportedTypes
        self.path = path

        for fileType in supportedTypes.split(","):
            for file in glob.glob(f"{path}*.{fileType}"):
                self.files.append(file)
    
    def foundFiles(self):
        return len(self.files) > 0

    def ask(self):
        self.question = MultipleChoiceQuestion("Pick a file", "", self.files)
        self.question.ask()
        return self
    
    def getValue(self):
        return self.question.getValue()

    def getIndex(self):
        return self.question.getIndex()

class OpenEndedQuestion:
    def __init__(self, query, description):
        self.query = query
        self.description = description
        self.ans = ""

    def ask(self):
        print(self.query)
        if len(self.description) != 0:
            print(f"({self.description})")
        
        self.ans = input("Enter: ")

        return self
    
    def getValue(self):
        return self.ans


class MultipleChoiceQuestion:
    def __init__(self, query, description, optionsArray):
        self.query = query
        self.description = description
        self.optionsArray = optionsArray
        self.ans = 0

    def ask(self):
        print(self.query)
        for i in range(len(self.optionsArray)):
            print(f"\t {i+1}. {self.optionsArray[i]}")
        if len(self.description) != 0:
            print(f"({self.description})")
        
        while(True):
            x = input("Enter: ")
            if x.isnumeric() and len(x) > 0:
                self.ans = int(x)
                if self.ans <= len(self.optionsArray) and self.ans > 0:
                    self.ans -= 1
                    break
            print("Invalid value. Please try again.")

        return self
    
    def getIndex(self):
        return self.ans
    
    def getValue(self):
        return self.optionsArray[self.ans]

    def addOption(self, option):
        self.optionsArray.append(option)
        return self

    def setOptions(self, optionArray):
        self.optionsArray = optionArray
        return self
    