# Author: Thomas Preston

import numpy as np
import matplotlib.pyplot as plt
from tkinter import *
import matplotlib.animation as animation

# def f(x, a, b, c):
#     return a*x**2+b*x*c

# xlist = np.linspace(-10, 10, num = 1000)
# xlist = np.arange(-1, 10.1, .1)

# ylist = f(xlist, 3, 1, 4)
class Calc():
    window_width = 300
    window_height = 500
    window_x = 1000
    window_y = 100
    background_colour = "#ffffff"

    text = ""
    nummemory = []
    symmemory = []
    def main(self):
        self.window = Tk()
        self.window.geometry("{0}x{1}+{2}+{3}".format(self.window_width, self.window_height, self.window_x, self.window_y))
        self.window.title("Calculator")
        self.window.resizable(False, False)
        self.window.configure(bg = self.background_colour)
        self.window.iconbitmap("Calc.ico")

    def draw(self):
        lblf = LabelFrame(self.window, bd = 0, bg = "white", fg = "white")
        lblf.grid(row = 0, column = 0, columnspan = 4)

        self.lbl = Label(lblf, text = self.text, bg = "white", fg = "black", font = "arial 20")
        self.lbl.grid(row = 0, column = 0, columnspan = 3)

        row = 1
        column = 3
        columnspan = 1
        width = 2
        for i in range(0, 10):
            if i == 9:
                column = 1
                columnspan = 3
                width = 5
            i = 9 - i
            btn = Button(self.window, text = i, font = "arial 25", bd = 4, bg = self.background_colour, activebackground = self.background_colour, command = lambda num = i: self.display(num), relief = RIDGE, fg = "black", width = width)
            btn.grid(row = row, column = column, columnspan = columnspan)
            if column == 1:
                column = 3
                row += 1
                continue
            column -= 1

        width = 2
        row = 1
        column = 4
        for i in ["÷", "×", "-", "+"]:
            btn = Button(self.window, text = i, font = "arial 25", bd = 4, bg = self.background_colour, activebackground = self.background_colour, command = lambda num = i: self.mem(num), relief = RIDGE, fg = "black", width = width)
            btn.grid(row = row, column = column)
            row += 1

        row = 1
        # btn = Button(self.window, text = "𝑥", font = "arial 25", bd = 4, bg = self.background_colour, activebackground = self.background_colour, command = lambda num = "𝑥": self.display(num), relief = RIDGE, fg = "black", width = width)
        # btn.grid(row = row, column = column+1)

        btn = Button(self.window, text = "sin(x*y*π)", font = "arial 20", bd = 4, bg = self.background_colour, activebackground = self.background_colour, command = self.maths, relief = RIDGE, fg = "black", width = 7)
        btn.grid(row = 5, column = 0, columnspan = 4)

    def plotGraph(self):
        self.𝑥 = np.arange(0.0, 2.0, 0.01)

    def display(self, num):
        if len(self.text) == 10:
            return
        self.text += str(num)
        self.lbl.configure(text = self.text)

    def mem(self, symbol):
        self.nummemory.append(int(self.text))
        self.symmemory.append(symbol)
        self.text = ""
        self.lbl.configure(text = self.text)

    def maths(self):
        if len(self.nummemory) < 1:
            self.nummemory.append(1)
        sum = self.nummemory[0]
        self.nummemory.pop(0)
        if len(self.nummemory) > 0 and len(self.symmemory) > 0:
            for num in self.nummemory:
                if self.symmemory[0] == "+":
                    sum = sum + num
                if self.symmemory[0] == "-":
                    sum = sum - num
                if self.symmemory[0] == "×":
                    sum = sum * num
                if self.symmemory[0] == "÷":
                    sum = sum / num
                self.symmemory.pop(0)
                print(sum)
        y = np.sin(self.x * sum * np.pi)
        
        self.lbl.configure(text = "")
        self.memory = ""
        self.sym = ""
        self.text = ""

        self.sety(y)

    def sety(self, y):
        # plt.figure(num = 0, dpi = 120)
        fig, ax = plt.subplots()
        ax.plot(self.𝑥, y)
        ax.set(xlabel='πr', ylabel='Amplitude')
        ax.grid()

        plt.show()

    def run(self):
        self.main()
        
        self.draw()

        self.plotGraph()
        
        self.window.mainloop()

ui = Calc()
ui.run()