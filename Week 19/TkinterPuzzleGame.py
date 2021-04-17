# Author: Thomas Preston

from tkinter import *
import config as c

class HangmanGUI():
    window_width = 800
    window_height = 500
    window_x = 200
    window_y = 100

    commands_width = 210
    commands_height = window_height
    commands_x = window_x + window_width + 10
    commands_y = window_y

    # commands2_x = commands_x + commands_width + 10
    # commands2_y = window_y

    inventory_height = 50
    inventory_x = window_x
    inventory_y = window_y + window_height + 40

    background_colour = "#303030"

    DEBUGMode = False

    def __init__(self):
        self.window = Tk()
        self.window.geometry("{0}x{1}+{2}+{3}".format(self.window_width, self.window_height, self.window_x, self.window_y))
        self.window.title("Puzzle Game")
        self.window.resizable(False, False)
        self.window.configure(bg = self.background_colour)
        # self.window.iconbitmap('Puzzleicon.ico')

        self.inventory = Toplevel(self.window)
        self.inventory.geometry("{0}x{1}+{2}+{3}".format(self.window_width, self.inventory_height, self.inventory_x, self.inventory_y))
        self.inventory.title("Inventory")
        self.inventory.resizable(False, False)
        self.inventory.configure(bg = self.background_colour)

        self.commands = Toplevel(self.window)
        self.commands.geometry("{0}x{1}+{2}+{3}".format(self.commands_width, self.commands_height, self.commands_x, self.commands_y))
        self.commands.title("Commands")
        self.commands.resizable(False, False)
        self.commands.configure(bg = self.background_colour)
        # self.commands.iconbitmap('Icon.ico')

        # self.commands2 = Toplevel(self.window)
        # self.commands2.geometry("{0}x{1}+{2}+{3}".format(self.commands_width, self.commands_height, self.commands2_x, self.commands2_y))
        # self.commands2.title("Commands")
        # self.commands2.resizable(False, False)
        # self.commands2.configure(bg = self.background_colour)
        # self.commands.iconbitmap('Icon.ico')

        self.window.focus_force()
    def draw(self):
        title = Label(self.window, text = 'Puzzle Game', font = 'Orbitron 50 bold', bg = self.background_colour)
        title.pack()

        title.config(foreground="white")

        self.canvas = Canvas(self.window, width=300, height=300, bg = self.background_colour, highlightthickness = 0)
        
        self.MapButtons()

        
        import DrawMap
        DrawMap.GameMap(self.player_location, self.canvas, self.NorthButton, c.Rooms[self.player_location]["Exits"]["North"]["State"], self.EastButton, c.Rooms[self.player_location]["Exits"]["East"]["State"], self.SouthButton, c.Rooms[self.player_location]["Exits"]["South"]["State"], self.WestButton, c.Rooms[self.player_location]["Exits"]["West"]["State"])
        self.canvas.place(x = 500, y = 150)
        
        self.button_draw()

        lblf = LabelFrame(self.window, text = "Text:", bd = 4, bg = self.background_colour, relief = RIDGE)
        lblf.configure(foreground = "white")
        lblf.place(x = 40, y = 100, width = 400, height = 300)

        self.lbl1 = Label(lblf, text = "", font = 'Orbitron 15', bg = self.background_colour, foreground = "white")
        # self.lbl1.place(x = 20, y = 100)
        self.lbl1.grid(row = 0, column = 0)

        self.lbl3 = Label(lblf, text = "", font = "Orbitron 12", bg = self.background_colour, foreground = "white")
        # self.lbl3.place(x = 20, y = 130)
        self.lbl3.grid(row = 1, column = 0)


        self.lbl2 = Label(self.window, text = "Map:", font = 'Orbitron 20', bg = self.background_colour, foreground = "white")
        self.lbl2.place(x = 515, y = 132)

        self.lbl5 = Label(self.inventory, text = "Inventory:", font = "Orbitron 15", bg = self.background_colour, foreground = "white")
        self.lbl5.place(x = 10, y = 10)

    def MapButtons(self):
        lbl4 = LabelFrame(self.commands, text = "Travel:", bd = 4, bg = self.background_colour, relief = RIDGE)
        lbl4.configure(foreground = "white")
        # lbl4.place(x = 5, y = 165, width = 195, height = 120)
        lbl4.grid(row = 3, column = 0)
        
        placeholder = Label(lbl4, text = "              ", bg = self.background_colour)
        placeholder.grid(row = 0, column = 0)

        placeholder2 = Label(lbl4, text = "            ", bg = self.background_colour)
        placeholder2.grid(row = 0, column = 4)

        self.NorthButton = Button(lbl4, text = "↑", font = "Orbitron 10", bd = 4, bg = self.background_colour, activebackground = self.background_colour, command = lambda direction = "North": self.go(direction), width = 2, relief = RIDGE, foreground = "white")
        # self.NorthButton.place(x = 103, y = 195, anchor = CENTER)
        self.NorthButton.grid(row = 0, column = 2)

        self.EastButton = Button(lbl4, text = "→", font = "Orbitron 10", bd = 4, bg = self.background_colour, activebackground = self.background_colour, command = lambda direction = "East": self.go(direction), width = 2, relief = RIDGE, foreground = "white")
        # self.EastButton.place(x = 175, y = 215, anchor = CENTER)
        self.EastButton.grid(row = 1, column = 3) 

        self.SouthButton = Button(lbl4, text = "↓", font = "Orbitron 10", bd = 4, bg = self.background_colour, activebackground = self.background_colour, command = lambda direction = "South": self.go(direction), width = 2, relief = RIDGE, foreground = "white")
        # self.SouthButton.place(x = 103, y = 245, anchor = CENTER)
        self.SouthButton.grid(row = 2, column = 2)

        self.WestButton = Button(lbl4, text = "←", font = "Orbitron 10", bd = 4, bg = self.background_colour, activebackground = self.background_colour, command = lambda direction = "West": self.go(direction), width = 2, relief = RIDGE, foreground = "white")
        # self.WestButton.place(x = 30, y = 215, anchor = CENTER)
        self.WestButton.grid(row = 1, column = 1)
        
    def button_draw(self):
        exitButton = Button(self.window, text = "Exit", bd = 4, bg = self.background_colour, activebackground = self.background_colour, command = exit, width = 12, relief = RIDGE)
        exitButton.configure(foreground = "white")
        exitButton.place(x = 10, y = 461)



        lblf = LabelFrame(self.commands, text = "Look Around", bd = 4, bg = self.background_colour, relief = RIDGE)
        lblf.configure(foreground = "white")
        # lblf.place(x = 5, y = 0, width = 195, height = 85)
        lblf.grid(row = 0, column = 0)

        exploreButton = Button(lblf, text = "Explore", bd = 4, bg = self.background_colour, activebackground = self.background_colour, command = self.explore, width = 24, relief = RIDGE)
        exploreButton.configure(foreground = "white")
        exploreButton.grid(row = 0, column = 0)

        self.searchButton = Button(lblf, text = "Search", bd = 4, bg = self.background_colour, activebackground = self.background_colour, command = self.search, width = 24, relief = RIDGE)
        self.searchButton.configure(foreground = "white")
        self.searchButton.grid(row = 1, column = 0)



        lblf2 = LabelFrame(self.commands, text = "Take", bd = 4, bg = self.background_colour, relief = RIDGE)
        lblf2.configure(foreground = "white")
        # lblf2.place(x = 5, y = 85, width = 195, height = 80)
        lblf2.grid(row = 1, column = 0)

        takeButton = Button(lblf2, text = "Take", bd = 4, bg = self.background_colour, activebackground = self.background_colour, command = self.take, width = 24, relief = RIDGE)
        takeButton.configure(foreground = "white")
        takeButton.grid(row = 0, column = 0)

        self.takeEntry = Entry(lblf2, width = 29, bd = 4, bg = self.background_colour, relief = RIDGE, foreground = "white")
        self.takeEntry.grid(row = 1, column = 0)

        

        lblf3 = LabelFrame(self.commands, text = "Interact with Inventory Items", bd = 4, bg = self.background_colour, relief = RIDGE)
        lblf3.configure(foreground = "white")
        # lblf3.place(x = 5, y = 285, width = 195, height = 175)
        lblf3.grid(row = 2, column = 0)

        useButton = Button(lblf3, text = "Use", bd = 4, bg = self.background_colour, activebackground = self.background_colour, command = self.use, width = 24, relief = RIDGE)
        useButton.configure(foreground = "white")
        useButton.grid(row = 0, column = 0)

        pickButton = Button(lblf3, text = "Pick Lock", bd = 4, bg = self.background_colour, activebackground = self.background_colour, command = self.pick, width = 24, relief = RIDGE)
        pickButton.configure(foreground = "white")
        pickButton.grid(row = 1, column = 0)

        lbl = Label(lblf3, text = "Item:                                                ", bg = self.background_colour)
        lbl.configure(foreground = "white")
        lbl.grid(row = 2, column = 0)

        self.useEntry = Entry(lblf3, width = 29, bd = 4, bg = self.background_colour, relief = RIDGE, foreground = "white")
        self.useEntry.grid(row = 3, column = 0)

        lbl2 = Label(lblf3, text = "Door Direction:    (To open doors)", bg = self.background_colour)
        lbl2.configure(foreground = "white")
        lbl2.grid(row = 4, column = 0)

        self.doorEntry = Entry(lblf3, width = 29, bd = 4, bg = self.background_colour, relief = RIDGE, foreground = "white")
        self.doorEntry.grid(row = 5, column = 0)


        placeholder3 = Label(self.commands, text = " ", bg = self.background_colour)
        placeholder3.grid(row = 4, column = 0)

        self.DEBUGButton = Button(self.commands, text = "ENABLE DEBUG MODE", bd = 4, bg = self.background_colour, activebackground = self.background_colour, command = self.DEBUG, width = 24, relief = RIDGE)
        self.DEBUGButton.configure(foreground = "white")
        # self.DEBUGButton.place(x = 10, y = 465)
        self.DEBUGButton.grid(row = 5, column = 0)



        # lblf4 = LabelFrame(self.commands2, text = "Crafting", bd = 4, bg = self.background_colour, relief = RIDGE)
        # lblf4.configure(foreground = "white")
        # lblf4.grid(row = 0, column = 0)

        # lbl3  = Label(lblf4, text = "Item 1:", bg = self.background_colour, foreground = "white")
        # lbl3.grid(row = 0, column = 0)

        # self.crafting1 = Entry(lblf4, width = 29, bd = 4, bg = self.background_colour, relief = RIDGE, foreground = "white")
        # self.crafting1.grid(row = 1, column = 0)

        # lbl4 = Label(lblf4, text = "Item 2:", bg = self.background_colour, foreground = "white")
        # lbl4.grid(row = 2, column = 0)

        # self.crafting2 = Entry(lblf4, width = 29, bd = 4, bg = self.background_colour, relief = RIDGE, foreground = "white")
        # self.crafting2.grid(row = 3, column = 0)

        # self.lbl5 = Label(lblf4, text = "Output:", bg = self.background_colour, foreground = "white")
        # self.lbl5.grid(row = 4, column = 0)

    def game(self):
        self.player_location = c.Player_Location

        
    def explore(self):
        self.lbl1.configure(text = "There is:")
        lst = []
        for key in c.Rooms[self.player_location]["Items"]:
            arg = "A " + str(key)
            if self.DEBUGMode == True: print(arg)
            lst.append(arg)
            if self.DEBUGMode == True: print(lst)
            text = ""
            for string in lst:
                string = string.replace("(", "")
                string = string.replace(")", "")
                string = string.replace("'", "")
                text = text + string + "\n"
                if self.DEBUGMode == True: print(text)
                self.lbl3.configure(text = "{0}".format(text))
        c.Explored[self.player_location] = 1
        self.searchButtonState()

    def search(self):
        self.lbl1.configure(text = "Found inside:")
        lst = []
        for key in c.Rooms[self.player_location]["Items"]:
            lst.append(c.Rooms[self.player_location]["Items"][key])
        if self.DEBUGMode == True: print(lst)
        text = ""
        for item in lst:
            if self.DEBUGMode == True: print(item)
            L = list(item)
            if self.DEBUGMode == True: print(L)
            for string in L:
                if string == ' ':
                    continue
                else:
                    text = text + string + "\n"
                    if self.DEBUGMode == True: print(text)

        self.lbl3.configure(text = "{0}".format(text))

    def take(self):
        input = self.takeEntry.get()
        for key in c.Rooms[self.player_location]["Items"]:
            if self.DEBUGMode == True: print(key)
            items = str(c.Rooms[self.player_location]["Items"][key])
            if input in items:
                dictionary = c.Rooms[self.player_location]["Items"][key]
                if self.DEBUGMode == True: print(dictionary)
                L = list(dictionary)
                L.remove(input)
                tup  = tuple(L)
                c.Rooms[self.player_location]["Items"].update({key: tup})

                c.Player_Inventory.append(input)
                if self.DEBUGMode == True: print(c.Player_Inventory)
        self.UpdateInventory()
        self.search()

    def searchButtonState(self):
        if c.Explored[self.player_location] == 0:
            self.searchButton.config(state = "disabled")
        else:
            self.searchButton.config(state = "normal")

    def go(self, direction):
        GoingTo = c.Rooms[self.player_location]['Exits'][direction]['Output']
        if self.DEBUGMode == True: print(GoingTo)
        self.player_location = GoingTo

        c.Player_Location = GoingTo
        self.canvas.delete('all')
        self.searchButtonState()

        import DrawMap
        DrawMap.GameMap(self.player_location, self.canvas, self.NorthButton, c.Rooms[self.player_location]["Exits"]["North"]["State"], self.EastButton, c.Rooms[self.player_location]["Exits"]["East"]["State"], self.SouthButton, c.Rooms[self.player_location]["Exits"]["South"]["State"], self.WestButton, c.Rooms[self.player_location]["Exits"]["West"]["State"])

    def UpdateInventory(self):
        self.lbl5.config(text = "Inventory: {0}".format(c.Player_Inventory))

    def pick(self):
        iteminput = self.useEntry.get()
        doorinput = self.doorEntry.get()
        num = self.player_location.replace('Room', '')
        doornum = doorinput + num
        if iteminput in c.Player_Inventory:
            if iteminput in c.Pick:
                if doorinput in c.outputRooms[self.player_location]:
                    if c.Rooms[self.player_location]['Exits'][doorinput]['State'] == 'Locked':
                        self.canvas.delete('all')
                        self.searchButtonState()
                        c.Player_Inventory.remove(iteminput)
                        self.UpdateInventory()
                        c.Rooms[self.player_location]['Exits'][doorinput].update({'State': 'Unlocked'})
                        link = c.linkedDoors[doornum]
                        number = ["1","2","3","4","5","6","7","8","9","0"]
                        for string in number:
                            link = link.replace(string, "")
                        out = c.Rooms[self.player_location]['Exits'][doorinput]['Output']
                        c.Rooms[out]['Exits'][link].update({'State': 'Unlocked'})
                        import DrawMap
                        DrawMap.GameMap(self.player_location, self.canvas, self.NorthButton, c.Rooms[self.player_location]["Exits"]["North"]["State"], self.EastButton, c.Rooms[self.player_location]["Exits"]["East"]["State"], self.SouthButton, c.Rooms[self.player_location]["Exits"]["South"]["State"], self.WestButton, c.Rooms[self.player_location]["Exits"]["West"]["State"])

    def use(self):
        iteminput = self.useEntry.get()
        doorinput = self.doorEntry.get()
        num = self.player_location.replace('Room', '')
        doornum = doorinput + num
        if iteminput in c.Player_Inventory:
            if iteminput in c.Key:
                if iteminput == c.Rooms[self.player_location]['Exits'][doorinput]['Key']:
                    if doorinput in c.outputRooms[self.player_location]:
                        if c.Rooms[self.player_location]['Exits'][doorinput]['State'] == 'Locked':
                            self.canvas.delete('all')
                            self.searchButtonState()
                            self.UpdateInventory()
                            c.Rooms[self.player_location]['Exits'][doorinput].update({'State': 'Unlocked'})
                            link = c.linkedDoors[doornum]
                            number = ["1","2","3","4","5","6","7","8","9","0"]
                            for string in number:
                                link = link.replace(string, "")
                            out = c.Rooms[self.player_location]['Exits'][doorinput]['Output']
                            c.Rooms[out]['Exits'][link].update({'State': 'Unlocked'})
                            import DrawMap
                            DrawMap.GameMap(self.player_location, self.canvas, self.NorthButton, c.Rooms[self.player_location]["Exits"]["North"]["State"], self.EastButton, c.Rooms[self.player_location]["Exits"]["East"]["State"], self.SouthButton, c.Rooms[self.player_location]["Exits"]["South"]["State"], self.WestButton, c.Rooms[self.player_location]["Exits"]["West"]["State"])

    def DEBUG(self):
        self.DEBUGMode = True
        self.DEBUGButton.config(state = "disabled")

    def run(self):
        self.game()
        self.draw()
        self.searchButtonState()
        self.window.mainloop()
    
ui = HangmanGUI()
ui.run()