# Author: Thomas Preston

# Items
Items1 = {
    'Cupboard': (' ', 'Banana', 'Apple', 'Carrot'), 
    'Drawer': (' ', 'Fork', 'Knife')
}

Items2 = {
    'Crate': (' ','Blue Key')
}

Items3 = {
    'Test2': (' ')
}

# Room1 Exits/Walls
North1 = {
    'State': 'Locked'
}
East1 = {
    'State': 'Locked',
    'Direction': 'East',
    'Output': 0,
    'Key': None
}
South1 = {
    'State': 'Locked'
}
West1 = {
    'State': 'Locked'
}

# Room2 Exits/Walls
North2 = {
    'State': 'Locked',
    'Direction': 'North',
    'Output': 0,
    'Key': 'Blue Key'
}
East2 = {
    'State': 'Locked'
}
South2 = {
    'State': 'Locked'
}
West2 = {
    'State': East1['State'],
    'Direction': 'West',
    'Output': 0,
    'Key': None
}

# Room 3 Exits/Walls
North3 = {
    'State': 'Locked'
}
East3 = {
    'State': 'Locked',
    'Direction': 'East',
    'Output': 0,
    'Key': None
}
South3 = {
    'State': North2['State'],
    'Direction': 'South',
    'Output': 0,
    'Key': North2['Key']
}
West3 = {
    'State': 'Locked'
}

# All Room1 Exits
Exits1 = {
    'North': North1,
    'East': East1,
    'South': South1,
    'West': West1
}

# All Room2 Exits
Exits2 = {
    'North': North2,
    'East': East2,
    'South': South2,
    'West': West2
}
Exits3 = {
    'North': North3,
    'East': East3,
    'South': South3,
    'West': West3
}

# All Room1
Room1 = {
    'Items': Items1,
    'Exits': Exits1
}

# All Room2
Room2 = {
    'Items': Items2,
    'Exits': Exits2
}

# All Room3
Room3 = {
    'Items': Items3,
    'Exits': Exits3
}

# All Rooms
Rooms = {
    'Room1': Room1,
    'Room2': Room2,
    'Room3': Room3
}

# Explored Rooms
Explored = {
    'Room1': 0,
    'Room2': 0,
    'Room3': 0
}

# Update
East1.update(Output = 'Room2')
West2.update(Output = 'Room1')

North2.update(Output = 'Room3')
South3.update(Output = 'Room2')

# PlayerInfo
Player_Inventory = []
Player_Location = 'Room1'

# Pickable Items
Pick = ['Knife']

Key = ['Blue Key']

# Room Doors
outputRooms = {
    'Room1': ('East'),
    'Room2': ('West', 'North'),
    'Room3': ('South', 'East')
}

# Linked Doors
linkedDoors = {
    'East1': 'West2',
    'North2': 'South3'
}