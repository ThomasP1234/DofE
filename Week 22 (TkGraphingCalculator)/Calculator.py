# Author: Thomas Preston

from tkinter import *

class Calc():
    window_width = 300
    window_height = 500
    window_x = 200
    window_y = 100

    background_colour = "#303030"

    text = ""

    def main(self):
        self.window = Tk()
        self.window.geometry("{0}x{1}+{2}+{3}".format(self.window_width, self.window_height, self.window_x, self.window_y))
        self.window.title("Calculator")
        self.window.resizable(False, False)
        self.window.configure(bg = self.background_colour)
        self.window.iconbitmap("Calc.ico")

    def draw(self):
        placeholder = Label(self.window, text = "           ", bg = self.background_colour, fg = self.background_colour)
        placeholder.grid(row = 0, column = 0, rowspan = 10)

        placeholder = Label(self.window, text = "           ", bg = self.background_colour, fg = self.background_colour)
        placeholder.grid(row = 0, column = 0)

        lblf = LabelFrame(self.window, bd = 5, relief = RIDGE, bg = "white", fg = "white")
        lblf.grid(row = 1, column = 1, columnspan = 4)

        self.lbl = Label(lblf, text = self.text, bg = "white", fg = "black", font = "arial 20")
        self.lbl.pack()

        placehold = Label(lblf, text = "                                                                  ", bg = "white", fg = "white")
        placehold.pack()

        placeholder2 = Label(self.window, text = " ", bg = self.background_colour, fg = self.background_colour)
        placeholder2.grid(row = 2, column = 1, columnspan = 3)

        # lblf2 = LabelFrame(self.window, bd = 0, bg = self.background_colour, fg = self.background_colour)
        # lblf2.grid(row = 4, column = 0, rowspan = 4, columnspan = 2)
        
        row = 3
        column = 3
        columnspan = 1
        width = 2
        for i in range(0, 10):
            if row == 6:
                column = 1
                columnspan = 2
                width = 5
            i = 9 - i
            btn = Button(self.window, text = i, font = "arial 25", bd = 4, bg = self.background_colour, activebackground = self.background_colour, command = lambda num = i: self.display(num), relief = RIDGE, fg = "white", width = width)
            btn.grid(row = row, column = column, columnspan = columnspan)
            if column == 1:
                column = 3
                row += 1
                continue
            column -= 1

        width = 2

        btn = Button(self.window, text = ".", font = "arial 25", bd = 4, bg = self.background_colour, activebackground = self.background_colour, command = None, relief = RIDGE, fg = "white", width = width)
        btn.grid(row = 6, column = 3)
        btn["state"] = DISABLED
        # lblf3 = LabelFrame(self.window, bd = 0, bg = self.background_colour, fg = self.background_colour)
        # lblf3.grid(row = 4, column = 2, rowspan = 5)

        row = 3
        column = 4
        for i in ["÷", "×", "-", "+"]:
            btn = Button(self.window, text = i, font = "arial 25", bd = 4, bg = self.background_colour, activebackground = self.background_colour, command = lambda sym = i: self.mem(sym), relief = RIDGE, fg = "white", width = width)
            btn.grid(row = row, column = column)
            row += 1

        btn = Button(self.window, text = "=", font = "arial 25", bd = 4, bg = self.background_colour, activebackground = self.background_colour, command = self.maths, relief = RIDGE, fg = "white", width = 2)
        btn.grid(row = 8, column = column)
    
    def display(self, num):
        if len(self.text) == 10:
            return
        self.text += str(num)
        self.lbl.configure(text = self.text)

    def mem(self, symbol):
        try:
            self.memory = int(self.text)
            self.sym = symbol
            self.text = ""
            self.lbl.configure(text = self.text)
        except:
            pass

    def maths(self):
        try:
            num1 = self.memory
            num2 = int(self.text)
            if self.sym == "+":
                answer = num1 + num2
            if self.sym == "-":
                answer = num1 - num2
            if self.sym == "×":
                answer = num1 * num2
            if self.sym == "÷":
                answer = num1 / num2
            self.lbl.configure(text = str(answer))
            self.memory = ""
            self.sym = ""
            self.text = ""
        except:
            pass

    def run(self):
        self.main()

        self.draw()

        self.window.mainloop()

ui = Calc()
ui.run()
