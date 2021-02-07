# Author: Thomas Preston

def GetFullnameFromData(data):
    return "{0} {1}".format(data["Firstname"], data["Lastname"])

def GetPersonData(data):
    return "Fullname is {0}, age {1}.".format(GetFullnameFromData(data), data["Age"])