# Author: Thomas Preston

from tkinter import *
import random

class HigherLower():
    window_width = 800
    window_height = 500
    window_x = 200
    window_y = 100

    background_colour = "#303030"
    deck = {}

    numcards = 8
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
        cards = []
        f = Frame(self.window)
        f.place(x = 100, y = 100)
        card1 = Label(f, image = "Deck\\Back.png")
        card2 = Label(f, image = "Deck\\Back")
        card3 = Label(f, image = "Deck\\Back")
        card4 = Label(f, image = "Deck\\Back")
        card5 = Label(f, image = "Deck\\Back")
        card6 = Label(f, image = "Deck\\Back")
        card7 = Label(f, image = "Deck\\Back")
        card8 = Label(f, image = "Deck\\Back")
        cards.append(card1)
        cards.append(card2)
        cards.append(card3)
        cards.append(card4)
        cards.append(card5)
        cards.append(card6)
        cards.append(card7)
        cards.append(card8)

        row = 0
        column = 0
        for card in cards:
            card.grid(row = row, column = column)
            if row == 3:
                row = 0
                column = 1

    def game(self):
        pass

    def run(self):
        self.main()

        self.addCards()
        self.shuffled = self.getShuffledDeck()
        # print(self.deck)
        print(self.shuffled)

        self.draw()
        self.game()

        self.window.mainloop()

ui = HigherLower()
ui.run()