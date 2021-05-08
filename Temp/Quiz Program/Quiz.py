# Author: Thomas Preston

from tkinter import *
import json
import random

class Quiz():
    window_width = 800
    window_height = 500
    window_x = 200
    window_y = 100

    background_colour = "#303030"
    def main(self):
        self.window = Tk()
        self.window.geometry("{0}x{1}+{2}+{3}".format(self.window_width, self.window_height, self.window_x, self.window_y))
        self.window.title("Quiz")
        self.window.resizable(False, False)
        self.window.configure(bg = self.background_colour)

    def getQuestions(self):
        filename = "Questions.json"
        fi = open(filename, "r")
        data = fi.read()
        jsondata = json.loads(data)

        

    def run(self):
        self.main()

        self.getQuestions()

        self.window.mainloop()

runQuiz = Quiz()
runQuiz.run()