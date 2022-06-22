from fileinput import filename
import json
import os
class Paper():
    def jget(filename : str, setting_name : str):
        with open(str(os.path.dirname(os.path.abspath(__file__)))+ r"/" + filename + ".json", "r") as jfile:
            try:
                return json.loads(jfile.read())[setting_name]
            except:
                return None

    def jdumpget(filename : str, settings):
        with open(str(os.path.dirname(os.path.abspath(__file__))) + r"/" + filename + ".json", "r") as jfile:
            output = {}
            data = json.loads(jfile.read())
            for key in settings:
                output[key] = data[key]
            return output
        
    def jset(filename : str, setting_name : str, setting_value):
        with open(str(os.path.dirname(os.path.abspath(__file__))) + r"/" + filename + ".json", "r") as jfile:
            directory = json.loads(jfile.read())
            directory[setting_name] = setting_value
        with open(str(os.path.dirname(os.path.abspath(__file__))) + r"/" + filename + ".json", "w") as jfile:
            json.dump(directory, jfile)

    def jdumpset(filename : str, settings):
        with open(str(os.path.dirname(os.path.abspath(__file__))) + r"/" + filename + ".json", "r") as jfile:
            directory = json.loads(jfile.read())
            for setting in settings.keys():
                directory[setting] = settings[setting]
        with open(str(os.path.dirname(os.path.abspath(__file__))) + r"/" + filename + ".json", "w") as jfile:
            json.dump(directory, jfile)

    def get_all_keys(filename : str):
        path = str(os.path.dirname(os.path.abspath(__file__)))
        with open(path + "/" + filename + ".json", "r") as jfile:
            directory : dict = json.loads(jfile.read())
            return directory.keys()

    def __init__(self, driver):
        self.driver = driver
        self.jsonprefixes = []
        for string in os.listdir:
            self.jsonprefixes.append(string.split(".")[0])
            with self.jdumpget(filename = string.split(".")[0], settings = self.get_all_keys(filename = string.split(".")[0])) as data:
                for key in data.keys():
                    setattr(self, string.split(".")[0] + "." + key, [])
        
    def changevalue(self, filename : str, name : str, value):
        self.jset(filename = filename, setting_name=name, setting_value=value)


