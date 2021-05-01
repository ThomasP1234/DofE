# HangmanV2GUI
# Author: Thomas Preston

from tkinter import *
import string
import HangmanV2Utils as utils

class HangmanGUI():
    window_width = 800
    window_background = "#dddddd"
    def __init__(self):
        self.window = Tk()
        self.window.geometry("{0}x500".format(HangmanGUI.window_width))
        self.window.title("Hangman")
        self.window.resizable(False, False)
        self.window.configure(bg=HangmanGUI.window_background)
        # self.window.wm_attributes('-transparentcolor','#00b140')
        self.letters = []
        for letter in list(string.ascii_uppercase):
            letter_state = {
                "letter": letter,
                "state": 0
            }
            self.letters.append(letter_state)
        self.buttons = []

    def draw(self):
        title = Label(self.window, text = 'Hangman', font = 'Orbitron 50 bold')
        title.configure(bg=HangmanGUI.window_background)
        title.pack()

        puzzleStr = utils.getPuzzleString()
        self.puzzleLabel = Label(self.window, text = puzzleStr, font = 'Orbitron 20 bold')
        self.puzzleLabel.configure(bg=HangmanGUI.window_background)
        self.puzzleLabel.place(relx = 0.5, rely = 0.25, anchor = 'center')

        xoffset = 50 
        yoffset = 175
        counter = 0
        for letter in self.letters:
            counter += 1
            self.add_alpha_button(xoffset, yoffset, letter)
            xoffset += 45
            if counter%6 == 0:
                xoffset = 50 
                yoffset += 45

        self.canvas = Canvas(self.window, width=300, height=250, bg = '#cccccc', highlightthickness = 0)
        self.canvas.place(x = 450, y = 175)

        exitButton = Button(self.window, text = "Exit", font = "Orbitron 10 bold", command = exit)
        exitButton.place(x = 2, y = 470)
    
    def add_alpha_button(self, xoffset, yoffset, l):
        f = Frame(self.window, width = 50, height = 50, borderwidth = 2, relief = "solid")
        b = Button(f, text = l["letter"], font = 'Orbitron 10 bold', width = 2, command = lambda: self.alpha_button_clicked(b, l))
        b.pack()
        self.buttons.append(b)
        f.place(x = xoffset, y = yoffset)
    
    def alpha_button_clicked(self, btn, l):
        btn["state"] = DISABLED
        btn.configure(fg = "white")

        l["state"] = utils.processGuess(l["letter"])
        if l["state"] == 3:
            #win
            btn.configure(bg = "lightgreen")
            self.disableAll()
            fr = Frame(self.window, width = 50, height = 50, borderwidth = 5, relief = "solid", highlightbackground = "black")
            outcome = Label(fr, text = 'Winner', font = 'Orbitron 100 bold', bg = "green", padx = 20)
            outcome.pack()
            fr.place(x = 400, y = 250, anchor="center")
        elif l["state"] == 2:
            #bad guess
            btn.configure(bg = "salmon")
        else:
            #good guess
            btn.configure(bg = "lightgreen")
        puzzleStr = utils.getPuzzleString()
        self.puzzleLabel.configure(text = puzzleStr)

        lost = self.drawHangman(utils.getStatus())
        if lost:
            self.disableAll()
            fr = Frame(self.window, width = 50, height = 50, borderwidth = 5, relief = "solid", highlightbackground = "black")
            outcome = Label(fr, text = 'Looser', font = 'Orbitron 100 bold', bg = "red", padx = 20)
            outcome.pack()
            fr.place(x = 400, y = 250, anchor="center")
    
    def drawHangman(self, itemNum):
        switcher = {
            1: lambda: self.canvas.create_line(15, 225, 285, 225, width = 5),
            2: lambda: self.canvas.create_line(75, 225, 75, 25, width = 5),
            3: lambda: self.canvas.create_line(75, 25, 175, 25, width = 5),
            4: lambda: self.canvas.create_line(175, 25, 175, 50, width = 2),
            5: lambda: self.canvas.create_oval(160, 50, 190, 85, outline = "black", width = 3),
            6: lambda: self.canvas.create_line(175, 85, 175, 145, width = 3),
            7: lambda: self.canvas.create_line(175, 85, 200, 130, width = 3),
            8: lambda: self.canvas.create_line(175, 85, 150, 130, width = 3),
            9: lambda: self.canvas.create_line(175, 145, 190, 200, width = 3),
            10: lambda: self.canvas.create_line(175, 145, 160, 200, width = 3),
        }
        switcher[itemNum]()
        lost = itemNum >= len(switcher.keys())
        return lost

    def run(self):
        self.draw()
        self.window.mainloop()
    
    def disableAll(self):
        for btn in self.buttons:
            btn["state"] = DISABLED
        
ui = HangmanGUI()
ui.run()
