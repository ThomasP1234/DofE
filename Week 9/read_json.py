# Author: Thomas Preston

import json
import PersonUtils as Utils

def ReadJson(filename):
    fi = open(filename, "r")
    data = fi.read()
    jsondata = json.loads(data)
    print("DEBUG:", type(data), type(jsondata))
    return jsondata

def ReadAndDisplayPersonDataFile(filename):
    data = ReadJson(filename)
    print("Read", data, "from", filename)
    print(Utils.GetPersonData(data))

filename = "data.json"

ReadAndDisplayPersonDataFile(filename)