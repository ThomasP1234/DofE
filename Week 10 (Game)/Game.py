# Word Adventure, Puzzle Game
# Author: Thomas Preston

playerlocation = "room 1"
door1 = "locked"
door2 = "locked"
inventory = []

def room1description():
    print('You are in room 1.')
    print('You are are in a plain room. The walls are whitewashed and the floor is polished wood.')
    print('There isn’t much furniture except and bed, a high shelf (probably out of reach) and a set of 3 drawers.')
    print('There is one solid door. There are no windows and it is lit by a bright light.')

def room2description():
    print('You are in room 2.')
    print('You enter the room and it is nice.')
    print('There is some nicely decorated wallpaper and a fresh carpet.') 
    print('There is a grand window on the one wall but then sun is bright and it is hard to see out.')
    print('There is a solid door going back to the original room and a locked, pristine, modern door going further on.')

def room3description():
    print('You are in room 3')
    print('The room is dark. It is lit by one floating candle.')
    print('There is a single shiny object 5 metres from the door but it is hard to make out what it is.')
    print('As you step into the room, the floor disappears but you dont fall, you float there.... weightless.')
    print('You are bewildered by the experience but must continue your adventure.')

print('Welcome to this word adventure, puzzle game made with python.')
print('For a list of commands, see COMMANDS.md')
print('')
print('Side Notes')
print('- Auto-unlock is on. Once you get a key. The door it unlocks opens.')
print('- Auto-pick up is on. If you find a object, you automatically put it in your inventory.')
print('- Make sure to read the text on-screen carefully as there might be some clues to help you on your adventure... good luck.')
print('')
print('You are are in a plain room. The walls are whitewashed and the floor is polished wood.')
print('There isn’t much furniture except a bed, a high shelf (probably out of reach) and a set of drawers.')
print('There is one solid door which is locked and requires a key. There are no windows and it is lit by a bright light.')

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
    elif action == "quit" or action == "q":
        print('Goodbye.')
        exit()
    else:
        print('Not an valid action.')
print('You have completed the game!!!')
print('Well done, you win!!!')
print('Thanks for playing!!!')