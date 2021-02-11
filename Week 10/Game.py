# Author: Thomas Preston

playerlocation = "room 1"
safetynet = 0
door1 = "locked"
inventory = []

print('Welcome to this word puzzle game made with python.')
print('For a list of commands, see COMMANDS.md')
print('')
print('You are are in a plain room. The walls are whitewashed and the floor is polished wood.')
print('There isn’t much furniture except and bed and a set of 3 drawers.')
print('There is one solid door which is locked and requires a key. There are no windows and it is lit by a bright light.')
print('')

while safetynet < 5:
    safetynet = safetynet + 1
    # print(saftynet)
    if "key" in inventory:
        door1 = "unlocked"
    action = input('What would you like to do?')
    if action == "move":
        movement = input('Where would you like to move to?')
        if movement == "room 1":
            print('You are in room 1')
            print('You are are in a plain room. The walls are whitewashed and the floor is polished wood.')
            print('There isn’t much furniture except and bed and a set of 3 drawers.')
            print('There is one solid door which is locked and requires a key. There are no windows and it is lit by a bright light.')
            print('')
        elif movement == "room 2" and door1 != "locked":
            playerlocation = "room 2"
            print('You are in room 2')
            print('You enter the room and it is nice.')
            print('There is some nicely decorated wallpaper and a fresh carpet.') 
            print('There is a grand window on the one wall but then sun is bright and it is hard to see out.')
        elif movement == "room 2" and door1 == "locked":
            print('The door is locked. Try looking for a key')
        else:
            print('Not a valid room you stayed where you were')
    elif action == "explore" and playerlocation == "room 1":
        print('There is a set of drawers.')
        drawersaction = input('What do you do?')
        if drawersaction == "open" and not ("key" in inventory):
            print('You find a key')
            inventory.append("key")
        elif drawersaction == "open" and "key" in inventory:
            print('Drawers are empty')
        elif drawersaction == "leave":
            print('You step away from the drawers')
        else:
            print('Not a valid action')
    elif action == "quit" or action == "q":
        print('goodbye')
        exit() 
    else:
        print('Not an valid action') 