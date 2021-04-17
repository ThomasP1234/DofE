# Author: Thomas Preston
lineColour = "white"
width = 3
door = 7
def GameMap(room, canvas, north, nstate, east, estate, south, sstate, west, wstate):
    north.config(state = "disabled")
    east.config(state = "disabled")
    south.config(state = "disabled")
    west.config(state = "disabled")

    canvas.create_text(273, 8, text = "N", font = "arial 20", fill = "red")
    canvas.create_line(273, 20, 273, 65, width = width, fill = lineColour)
    canvas.create_line(273, 20, 264, 35, width = width, fill = lineColour)
    canvas.create_line(273, 20, 282, 35, width = width, fill = lineColour)

    canvas.create_oval(122, 102, 143, 123, outline = "red", fill = "red")

    if room == "Room1":
        DrawNorthWall(canvas)
        DrawEastDoor(canvas, estate, east)
        DrawSouthWall(canvas)
        DrawWestWall(canvas)

    if room == "Room2":
        DrawNorthDoor(canvas, nstate, north)
        DrawEastWall(canvas)
        DrawSouthDoor(canvas, sstate, south)
        DrawWestDoor(canvas, wstate, west)

    if room == "Room3":
        DrawNorthWall(canvas)
        DrawEastDoor(canvas, estate, north)
        DrawSouthDoor(canvas, sstate, south)
        DrawWestWall(canvas)

    if room == "Room4":
        DrawNorthDoor(canvas, nstate, north)
        DrawEastDoor(canvas, estate, east)
        DrawSouthWall(canvas)
        DrawWestWall(canvas)   

def EndMap(canvas, north, east, south, west):
    north.config(state = "disabled")
    east.config(state = "disabled")
    south.config(state = "disabled")
    west.config(state = "disabled")

    DrawNorthWall(canvas)
    DrawEastWall(canvas)
    DrawSouthWall(canvas)
    DrawWestWall(canvas)

    canvas.create_text(130, 110, text = "You Win!!!", font = "Orbitron 30", fill = "red")

def DrawNorthWall(canvas):
    canvas.create_line(15, 25, 250, 25, width = width, fill = lineColour)

def DrawEastWall(canvas):
    canvas.create_line(250, 25, 250, 200, width = width, fill = lineColour)

def DrawSouthWall(canvas):
    canvas.create_line(15, 200, 250, 200, width = width, fill = lineColour)

def DrawWestWall(canvas):
    canvas.create_line(15, 25, 15, 200, width = width, fill = lineColour)

# door length = 55

def DrawNorthDoor(canvas, state, north):
    canvas.create_line(15, 25, 105, 25, width = width, fill = lineColour)
    canvas.create_line(160, 25, 250, 25, width = width, fill = lineColour)

    if state == "Locked":
        canvas.create_line(105, 25, 160, 25, width = door, fill = lineColour)

    if state == "Unlocked":
        canvas.create_line(105, 25, 135, 0, width = door, fill = lineColour)
        north.config(state = "normal")

def DrawEastDoor(canvas, state, east):
    canvas.create_line(250, 25, 250, 85, width = width, fill = lineColour)
    canvas.create_line(250, 200, 250, 140, width = width, fill = lineColour)

    if state == "Locked":
        canvas.create_line(250, 85, 250, 140, width = door, fill = lineColour)

    if state == "Unlocked":    
        canvas.create_line(250, 85, 275, 120, width = door, fill = lineColour)
        east.config(state = "normal")

def DrawSouthDoor(canvas, state, south):
    canvas.create_line(15, 200, 105, 200, width = width, fill = lineColour)
    canvas.create_line(160, 200, 250, 200, width = width, fill = lineColour)

    if state == "Locked":
        canvas.create_line(105, 200, 160, 200, width = door, fill = lineColour)

    if state == "Unlocked":
        canvas.create_line(105, 200, 135, 225, width = door, fill = lineColour)
        south.config(state = "normal")

def DrawWestDoor(canvas, state, west):
    canvas.create_line(15, 25, 15, 85, width = width, fill = lineColour)
    canvas.create_line(15, 200, 15, 140, width = width, fill = lineColour)

    if state == "Locked":
        canvas.create_line(15, 85, 15, 140, width = door, fill = lineColour)

    if state == "Unlocked":    
        canvas.create_line(15, 85, 40, 120, width = door, fill = lineColour)
        west.config(state = "normal")