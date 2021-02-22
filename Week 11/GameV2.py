# Word Adventure, Puzzle Game
# Author: Thomas Preston

import json
from RoomDescriptions import *
from Intro import *

filename = "GameSave.json"
playerlocation = "room 1"
door1 = "locked"
door2 = "locked"
inventory = []

data = {
    "playerlocation" : playerlocation,
    "inventory" : inventory
}

def Save(filename, data):
    with open(filename, 'w') as outfile:
        json.dump(data, outfile)

def Load(filename):
    fi = open(filename, "r")
    data = fi.read()
    global jsondata
    jsondata = json.loads(data)
    # print("DEBUG:", type(data), type(jsondata)) # Debug Line

introduction()

while True:
    if "key1" in inventory:
        door1 = "unlocked"
    if "key2" in inventory:
        door2 = "unlocked"
    action = input('\nWhat would you like to do? ')
    if action == "move":
        movement = input('Where would you like to move to? ')
        if movement == "room 1":
            playerlocation = "room 1"
            room1description()
        elif movement == "room 2" and door1 != "locked":
            playerlocation = "room 2"
            room2description()
        elif movement == "room 2" and door1 == "locked":
            print('The door is locked. Try looking for a key.')
        elif movement == "room 3" and door2 != "locked":
            playerlocation = "room 3"
            print('You are in room 3.')
            room3description()
        elif movement == "room 3" and door2 == "locked":
            print('The door is locked. Try looking for a key.')
        else:
            print('Not a valid place, you stayed where you were.')
    elif action == "explore" and playerlocation == "room 1" and not ("ladder" in inventory):
        print('There is a set of drawers.')
        drawersaction = input('What do you do? ')
        if drawersaction == "open" and not ("key1" in inventory):
            print('You find a key.')
            inventory.append("key1")
        elif drawersaction == "open" and "key1" in inventory:
            print('Drawers are empty.')
        elif drawersaction == "leave":
            print('You step away from the drawers.')
        else:
            print('Not a valid action.')
    elif action == "explore" and playerlocation == "room 2":
        print('There is a trapdoor underneath the carpet.')
        drawersaction == input('What do you do? ')
        if drawersaction == "open":
            print('You found a small crate with a different sized key in.')
            inventory.append("key2")
        elif drawersaction == "leave":
            print('You step away from the trapdoor and put the carpet back.')
        else:
            print('Not a valid action.')
    elif action == "explore" and playerlocation == "room 3":
        print('You find a ladder.')
        inventory.append("ladder")
    elif action == "explore" and playerlocation == "room 1" and "ladder" in inventory:
        print('Up on the high shelf, you find a strange device.')
        print('The moment you touch it, you get wizzed away back home and are happy to be back.')
        print('')       
        break
    elif action == "save":
        Save(filename, data)
        print("Game saved")
    elif action == "load":
        Load(filename)
        playerlocation = jsondata["playerlocation"]
        inventory = jsondata["inventory"]
        print("Game loaded")
        print("playerlocation: ", playerlocation)
        print("inventory: ", inventory)
    elif action == "info":
        print("playerlocation: ", playerlocation)
        print("inventory: ", inventory)
    elif action == "quit" or action == "q":
        print('Goodbye.')
        exit()
    else:
        print('Not an valid action.')
print('You have completed the game!!!')
print('Well done, you win!!!')
print('Thanks for playing!!!')
