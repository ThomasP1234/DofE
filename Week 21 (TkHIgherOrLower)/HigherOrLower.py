# Author: Thomas Preston

from tkinter import *
import random
from PIL import ImageTk, Image

# Todo
# Play Again Button

class HigherLower():
    window_width = 800
    window_height = 500
    window_x = 200
    window_y = 100

    background_colour = "#303030"
    deck = {}

    numcards = 8

    score = 0
    def main(self):
        self.window = Tk()
        self.window.geometry("{0}x{1}+{2}+{3}".format(self.window_width, self.window_height, self.window_x, self.window_y))
        self.window.title("Higher Or Lower")
        self.window.resizable(False, False)
        self.window.configure(bg = self.background_colour)

    def addCards(self):
        for i in range(1, 14):
            cardValue = str(i)
            if i == 1: # Ace is Low
                cardValue = "Ace"
            if i == 11:
                cardValue = "Jack"
            if i == 12:
                cardValue = "Queen"
            if i == 13:
                cardValue = "King"
            for suit in ["Spade", "Club", "Heart", "Diamond"]:
                self.deck[suit + cardValue]=i

    def getShuffledDeck(self):
        shuffledDeck = list(self.deck.keys())
        random.shuffle(shuffledDeck)
        return shuffledDeck

    def draw(self):
        title = Label(self.window, text = 'Higher or Lower', font = 'Orbitron 50 bold')
        title.configure(bg = self.background_colour, fg = "white")
        title.pack()

        f = Frame(self.window, bg = self.background_colour)
        # f.place(x = 200, y = 100)
        f.pack()
        img = Image.open("Deck\\Back.png")
        img = img.resize((93, 135), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        self.card1 = Label(f, image = img, bg = self.background_colour)
        self.card2 = Label(f, image = img, bg = self.background_colour)
        self.card3 = Label(f, image = img, bg = self.background_colour)
        self.card4 = Label(f, image = img, bg = self.background_colour)
        self.card5 = Label(f, image = img, bg = self.background_colour)
        self.card6 = Label(f, image = img, bg = self.background_colour)
        self.card7 = Label(f, image = img, bg = self.background_colour)
        self.card8 = Label(f, image = img, bg = self.background_colour)

        self.card1.image = img
        self.card1.grid(row = 0, column = 0)

        self.card2.image = img
        self.card2.grid(row = 0, column = 1)

        self.card3.image = img
        self.card3.grid(row = 0, column = 2)

        self.card4.image = img
        self.card4.grid(row = 0, column = 3)

        self.card5.image = img
        self.card5.grid(row = 1, column = 0)

        self.card6.image = img
        self.card6.grid(row = 1, column = 1)

        self.card7.image = img
        self.card7.grid(row = 1, column = 2)

        self.card8.image = img
        self.card8.grid(row = 1, column = 3)
        
        self.cards = []
        self.cards.append(self.card1)
        self.cards.append(self.card2)
        self.cards.append(self.card3)
        self.cards.append(self.card4)
        self.cards.append(self.card5)
        self.cards.append(self.card6)
        self.cards.append(self.card7)
        self.cards.append(self.card8)

        f2 = LabelFrame(self.window, bg = self.background_colour, fg = self.background_colour, bd = 0)
        f2.pack()

        self.b1 = Button(f2, text = "Higher", bd = 4, bg = self.background_colour, fg = "white", activebackground = self.background_colour, command = lambda playerinput = "H": self.game(playerinput), width = 22, relief = RIDGE)
        # b1.place(x = 300, y = 300)
        self.b1.grid(row = 0, column = 0)

        self.b2 = Button(f2, text = "Lower", bd = 4, bg = self.background_colour, fg = "white", activebackground = self.background_colour, command = lambda playerinput = "L": self.game(playerinput), width = 22, relief = RIDGE)
        self.b2.grid(row = 0, column = 1)

        self.label = Label(self.window, text = "", font = 'Orbitron 20', bg = self.background_colour, fg = "white")
        self.label.pack()

        self.scorelbl = Label(self.window, text = "Score: {0}".format(self.score), font = 'Orbitron 15', bg = self.background_colour, fg = "white")
        self.scorelbl.place(x = 10, y = 80)

        b3 = Button(self.window, text = "Quit", command = exit, bd = 4, bg = self.background_colour, fg = "white", activebackground = self.background_colour, height = 1, relief = RIDGE)
        b3.place(x = 750, y = 465)

    def setup(self):
        uicard = self.cards.pop(0)
        self.card = self.shuffled.pop(0)
        img = Image.open("Deck\\{0}.png".format(self.card))
        img = img.resize((93, 135), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        uicard.config(image = img)
        uicard.image = img

    def game(self, input):
        uicard = self.cards.pop(0)
        self.nextCard = self.shuffled.pop(0)
        img = Image.open("Deck\\{0}.png".format(self.nextCard))
        img = img.resize((93, 135), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        uicard.config(image = img)
        uicard.image = img

        if self.deck[self.nextCard] == self.deck[self.card]:
            self.label.config(text = "Equal Card Value - You loose\nEnd Score = {0}".format(self.score))
            self.b1["state"] = DISABLED
            self.b2["state"] = DISABLED

        elif self.deck[self.nextCard] > self.deck[self.card] and input == "H":
            self.label.config(text = "Higher - Well done")
            self.score += 1
            self.scorelbl.config(text = "Score: {0}".format(self.score))

        elif self.deck[self.nextCard] < self.deck[self.card] and input == "L":
            self.label.config(text = "Lower - Well done")
            self.score += 1
            self.scorelbl.config(text = "Score: {0}".format(self.score))
        
        else:
            self.label.config(text = "Wrong - You loose\nEnd Score = {0}".format(self.score))
            self.b1["state"] = DISABLED
            self.b2["state"] = DISABLED

        if len(self.cards) == 0:
            self.label.config(text = "You Win... No Cards Remaining\nEnd Score = {0}".format(self.score))
            self.b1["state"] = DISABLED
            self.b2["state"] = DISABLED

        self.card = self.nextCard

    def run(self):
        self.main()

        self.addCards()
        self.shuffled = self.getShuffledDeck()

        self.draw()

        self.setup()
        # print(self.deck)
        # print(self.shuffled)

        self.window.mainloop()

ui = HigherLower()
ui.run()