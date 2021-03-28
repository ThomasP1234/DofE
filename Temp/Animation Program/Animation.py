# Author: Thomas Preston

from tkinter import *


class Animation():
    def main(self):
        # Variables for all
        self.background_colour = "#303030"
        # Root
        self.root_width = 800
        self.root_height = 500
        self.root_height2 = self.root_height+75

        self.root = Tk()
        self.root.geometry("{0}x{1}+280+175".format(self.root_width, self.root_height2))
        self.root.title("Animation Window")
        self.root.resizable(False, False)
        self.root.configure(bg=self.background_colour)

        self.root.iconbitmap('Play.ico')

        self.c = Canvas(self.root, bg = "white", bd = 5, relief = GROOVE, height = self.root_height-35, width = self.root_width-35)
        self.c.place(x = 10, y = 10)

        # Secondary Window(s)
        self.test_width = 300
        self.test_height = 575

        self.test = Tk()
        self.test.geometry("{0}x{1}+1100+175".format(self.test_width, self.test_height))
        self.test.title("Test")
        self.test.resizable(False, False)
        self.test.configure(bg=self.background_colour)

        self.test.iconbitmap('Play.ico')

        # Run
        self.root.mainloop()

    # Methods

ui = Animation()
ui.main()