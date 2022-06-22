from fileinput import filename
import json
import os
class Paper():
    def jget(self, filename : str, setting_name : str):
        with open(str(os.path.dirname(os.path.abspath(__file__)))+ r"/Files/" + filename + ".json", "r") as jfile:
            try:
                return json.loads(jfile.read())[setting_name]
            except:
                return None

    def jdumpget(self, filename : str, settings):
        with open(str(os.path.dirname(os.path.abspath(__file__))) + r"/Files/" + filename + ".json", "r") as jfile:
            output = {}
            data = json.loads(jfile.read())
            for key in settings:
                output[key] = data[key]
            return output
        
    def jset(self, filename : str, setting_name : str, setting_value):
        with open(str(os.path.dirname(os.path.abspath(__file__))) + r"/Files/" + filename + ".json", "r") as jfile:
            directory = json.loads(jfile.read())
            directory[setting_name] = setting_value
        with open(str(os.path.dirname(os.path.abspath(__file__))) + r"/Files/" + filename + ".json", "w") as jfile:
            json.dump(directory, jfile)

    def jdumpset(self, filename : str, settings):
        with open(str(os.path.dirname(os.path.abspath(__file__))) + r"/Files/" + filename + ".json", "r") as jfile:
            directory = json.loads(jfile.read())
            for setting in settings.keys():
                directory[setting] = settings[setting]
        with open(str(os.path.dirname(os.path.abspath(__file__))) + r"/Files/" + filename + ".json", "w") as jfile:
            json.dump(directory, jfile)

    def get_all_keys(self, filename : str):
        path = str(os.path.dirname(os.path.abspath(__file__)))
        with open(path + r"/Files/" + filename + ".json", "r") as jfile:
            directory : dict = json.loads(jfile.read())
            return directory.keys()

    def __init__(self, driver, custommainloopactions = None):
        self.driver = driver
        self.jsonprefixes = []
        for string in os.listdir(str(os.path.dirname(os.path.abspath(__file__))) + r"/Files/"):
            self.jsonprefixes.append(string.split(".")[0])
            data = self.jdumpget(filename = string.split(".")[0], settings = self.get_all_keys(filename = string.split(".")[0]))
            for key in data.keys():
                setattr(self, string.split(".")[0] + "." + key, [])
        self.custommainloopactions = custommainloopactions
        self.loop()
        
    def changevalue(self, filename : str, name : str, value):
        self.jset(filename = filename, setting_name=name, setting_value=value)

    def loop(self):
        attributes = self.__dict__
        while True:
            for attribute in self.__dict__:
                if attributes[attribute] != getattr(self, attribute):
                    pass
                    #Manage what happens when variable has changed
            attributes = self.__dict__
            if self.custommainloopactions != None : self.custommainloopactions()



