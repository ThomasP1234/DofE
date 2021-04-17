# Author: Thomas Preston

# Items
Items1 = {
    'Cupboard': (' ', 'Banana', 'Apple', 'Carrot'), 
    'Drawer': (' ', 'Fork', 'Knife')
}

Items2 = {
    'Crate': (' ', 'Blue Key')
}

Items3 = {
    'Wall Safe': (' ', 'Green Key')
}

Items4 = {
    'Desk Drawer': (' ', 'Red Key')
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
    'State': 'Locked',
    'Direction': 'South',
    'Output': 0,
    'Key': 'Green Key'
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

# Room 4 Exits/Walls
North4 = {
    'State': South2['State'],
    'Direction': 'North',
    'Output': 0,
    'Key': South2['Key']
}
East4 = {
    'State': 'Locked',
    'Direction': 'East',
    'Output': 0,
    'Key': 'Master Key'
}
South4 = {
    'State': 'Locked'
}
West4 = {
    'State': 'Locked'
}

Exit = {
    'State': East4['State'],
    'Direction': 'West',
    'Output': 0,
    'Key': East4['Key']
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

# All Room3 Exits
Exits3 = {
    'North': North3,
    'East': East3,
    'South': South3,
    'West': West3
}

# All Room4 Exits
Exits4 = {
    'North': North4,
    'East': East4,
    'South': South4,
    'West': West4
}

# All RoomExit Exits
ExitsE = {
    'West': 'Exit'
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

# All Room4
Room4 = {
    'Items': Items4,
    'Exits': Exits4
}

# Exit Room
Exit = {
    'Exits': ExitsE
}

# All Rooms
Rooms = {
    'Room1': Room1,
    'Room2': Room2,
    'Room3': Room3,
    'Room4': Room4,
    'Exit': Exit
}

# Explored Rooms
Explored = {
    'Room1': 0,
    'Room2': 0,
    'Room3': 0,
    'Room4': 0,
    'Exit': 1
}

# Update
East1.update(Output = 'Room2')
West2.update(Output = 'Room1')

North2.update(Output = 'Room3')
South3.update(Output = 'Room2')

South2.update(Output = 'Room4')
North4.update(Output = 'Room2')

East4.update(Output = 'Exit')
Exit.update(Output = 'Exit')

# PlayerInfo
Player_Inventory = []
Player_Location = 'Room1'

# Items that have special properties
Pick = ['Knife']

Key = ['Blue Key', 'Green Key', 'Red Key', 'Master Key']

Crafts3 = {
    'Master Key': ('Blue Key', 'Green Key', 'Red Key')
}
Craftable3 = ['Master Key']
Craftitems = ['Blue Key', 'Green Key', 'Red Key']

# Room Doors
outputRooms = {
    'Room1': ('East'),
    'Room2': ('West', 'North', 'South'),
    'Room3': ('South', 'East'),
    'Room4': ('North', 'East')
}

# Linked Doors
linkedDoors = {
    'East1': 'West2',
    'North2': 'South3',
    'South2': 'North4',
    'East4': 'Exit'
}