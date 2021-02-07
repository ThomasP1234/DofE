# Author: Thomas Preston

import json
import PersonUtils as Utils

data = {
    "Firstname": "John",
    "Lastname": "Smith",
    "Age": 27,
    "DateOfBirth": "1994-01-21" # Using strings for dates (YYYY-MM-DD)
}
 

def WriteJson(filename, data):
    with open(filename, 'w') as outfile:
        json.dump(data, outfile)

filename = "data.json"

print(Utils.GetPersonData(data))

WriteJson(filename, data)

print("Written", data, "to", filename)