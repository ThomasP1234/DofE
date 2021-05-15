# Author: Thomas Preston

from tkinter import *
import json
import random

class Quiz():
    window_width = 300
    window_height = 500
    window_x = 200
    window_y = 100

    background_colour = "#303030"

    score = 0
    timer = 10

    played = []

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
        # print(data, "\n", jsondata)
        self.numquestion = jsondata["Amount"]
        self.questions = jsondata
        # print(self.numquestion)
        # print(self.questions)

    def draw(self):
        title = Label(self.window, text = "Quiz", font = "Orbitron 50 bold", bg = self.background_colour, fg = "white")
        title.grid(row = 0, column = 0)

        frame =  LabelFrame(self.window, text = "Question:", font = "Orbitron 18 bold", bg = self.background_colour, fg = "white", width = 280, height = 200, bd = 5)
        frame.grid(row = 1, column = 0)

        self.mainframe = Frame(self.window, bg = self.background_colour, width = 300, height = 400)
        self.mainframe.grid(row = 2, column = 0)

        frame2 = Frame(self.window, bg = self.background_colour, width = 300, height = 100)
        frame2.grid(row = 3, column = 0)

        self.scorelabel = Label(frame2, text = "Score: {}".format(self.score), font = "Orbitron 20 bold", bg = self.background_colour, fg = "white")
        self.scorelabel.place(x = 5, y = 0)

        self.question = Label(frame, text = "", font = "Orbitron 15 bold", bg = self.background_colour, fg = "white")
        self.question.place(x = 5, y = 0)

    def game(self):
        self.questionnum = random.choice(range(1, self.numquestion+1))
        self.scorelabel.config(text = "Score: {}".format(self.score))
        if len(self.played) == self.numquestion:
            self.question.config(text = "Out of Questions - \nFinal Score: {}".format(self.score))
        elif self.questionnum in self.played:
            self.game()
        else:
            # print(questiondata)
            questiondata = self.questions[str(self.questionnum)]["Q"]
            self.question.config(text = questiondata)

            del self.questions[str(self.questionnum)]["Q"]
            for key in self.questions[str(self.questionnum)]:
                answer = Button(self.mainframe, text = key, font = "orbitron 15", bg = self.background_colour, activebackground = self.background_colour, fg = "white", width = 10, bd = 3, command = lambda answer = key: self.check(answer))
                answer.pack()
            self.played.append(self.questionnum)

    def check(self, answer):
        if self.questions[str(self.questionnum)][answer] == "True":
            self.score += 1
        else:
            pass

        self.question.config(text = "")
        self.mainframe.destroy()

        self.mainframe = Frame(self.window, bg = self.background_colour, width = 300, height = 400)
        self.mainframe.grid(row = 2, column = 0)

        self.game()

    def run(self):
        self.main()

        self.getQuestions()

        self.draw()

        self.game()

        self.window.mainloop()

runQuiz = Quiz()
runQuiz.run()