# Author: Thomas Preston

from tkinter import *
import random
from PIL import Image, ImageTk

class RPS():
    background_colour = "#303030"
    window_width = 800
    window_height = 600
    window_x = 300
    window_y = 150

    score1 = 0
    score2 = 0

    def main(self):
        self.window = Tk()
        self.window.geometry("{0}x{1}+{2}+{3}".format(self.window_width, self.window_height, self.window_x, self.window_y))
        self.window.title("Rock Paper Scissors")
        self.window.resizable(False, False)
        self.window.configure(bg=self.background_colour)

    def draw(self):
        title = Label(self.window, text = "Rock Paper Scissors", font = 'Orbitron 40 bold', bg = self.background_colour, fg = "white")
        title.pack()

        frame1 = Frame(self.window, bg = self.background_colour)
        frame1.place(x = 10, y = 80)

        instuctionbtn = Button(frame1, text = "How to play", font = 'Arial 15', bg = self.background_colour, fg = "white", activebackground = self.background_colour, bd = 2, relief = RIDGE, command = self.instructions)
        instuctionbtn.pack()

        self.scorelbl = Label(frame1, justify= LEFT, text = "Your Score: {}\nComputer Score: {}".format(self.score1, self.score2), font = 'Arial 10', bg = self.background_colour, fg = "white")
        self.scorelbl.pack()

        quit = Button(self.window, text = "Quit", font = 'Arial 15', bg = self.background_colour, fg = "white", activebackground = self.background_colour, bd = 2, relief = RIDGE, command = exit)
        quit.place(x = 735, y = 15)

        self.textlbl = Label(self.window, text = "", font = 'Arial 15', bg = self.background_colour, fg = "white")
        self.textlbl.pack()


        frame2 = Frame(self.window, bg = self.background_colour)
        frame2.pack()

        column = 0
        for i in ["Rock", "Paper", "Scissors"]:
            btn = Button(frame2, text = i, font = 'Arial 15', bg = self.background_colour, fg = "white", activebackground = self.background_colour, bd = 2, relief = RIDGE, command = lambda text = i: self.game(text), width = 7)
            btn.grid(row = 0, column = column, padx = 5)
            column += 1

        self.label1 = Label(bg = self.background_colour)
        self.label2 = Label(bg = self.background_colour)

        self.lbl1 = Label(self.window, text = "", font = 'Arial 15', bg = self.background_colour, fg = "white")
        self.lbl2 = Label(self.window, text = "", font = 'Arial 15', bg = self.background_colour, fg = "white")

        self.lbl1.pack()
        self.label1.pack()
        self.lbl2.pack()
        self.label2.pack()

    def imageDraw(self, one, two):
        self.lbl1.config(text = "You:")
        self.lbl2.config(text = "Computer:")

        image1 = Image.open(one + ".png")
        image2 = Image.open(two + ".png")

        image1 = image1.resize((225, 175), Image.ANTIALIAS)
        image2 = image2.resize((225, 175), Image.ANTIALIAS)

        img1 = ImageTk.PhotoImage(image1)
        img2 = ImageTk.PhotoImage(image2)

        self.label1.configure(image = img1)
        self.label2.configure(image = img2)

        self.label1.image = img1
        self.label2.image = img2

    def popup(self, msg):
        x = (self.window_x + self.window_width/2) - 300
        y = (self.window_y + self.window_height/2) - 200
        popup = Toplevel()
        popup.geometry("650x300+{}+{}".format(int(x), int(y)))
        popup.configure(bg = "white")

        popuplbl = Label(popup, justify = LEFT, text = msg, font = 'Arial 15', bg = "white", fg = "black")
        popuplbl.place(x = 0, y = 0)

        popupbtn = Button(popup, text = "Ok", font = 'Arial 10', command = popup.destroy)
        popupbtn.place(x = 290, y = 250)

    def instructions(self):
        text = """
        This is a game of rock, paper, scissors.
        You choose one of the 3 options.
        What you choose determines whether you win, loose or draw.
        If you and the computer choose the same then it is a draw.
        Win conditions:
        - Rock crushes Scissors
        - Scissors cuts Paper
        - Paper covers Rock
        """
        self.popup(text)

    def game(self, input):
        computer = random.choice(["Rock", "Paper", "Scissors"])

        self.imageDraw(input, computer)

        if input == computer:
            self.textlbl.config(text = "Draw, Computer Chose {}".format(computer))
        elif input == "Rock" and computer == "Scissors":
            self.textlbl.config(text = "You Win, Computer Chose {}".format(computer))
            self.score1 += 1
        elif input == "Paper" and computer == "Rock":
            self.textlbl.config(text = "You Win, Computer Chose {}".format(computer))
            self.score1 += 1
        elif input == "Scissors" and computer == "Paper":
            self.textlbl.config(text = "You Win, Computer Chose {}".format(computer))
            self.score1 += 1
        else:
            self.textlbl.config(text = "You Loose, Computer Chose {}".format(computer))
            self.score2 += 1

        self.scorelbl.config(text = "Your Score: {}\nComputer Score: {}".format(self.score1, self.score2))
        

    def run(self):
        self.main()

        self.draw()


        self.window.mainloop()

UI = RPS()
UI.run()