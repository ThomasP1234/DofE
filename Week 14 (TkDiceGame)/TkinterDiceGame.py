from tkinter import *
import random
from PIL import ImageTk, Image
# py -m pip install pillow
import json

log = False

def dump(str):
    if log:
        print(str)

rules = """
The rules are:
• The points rolled on your dice are added to your score.
• If the total of the dice is an even number, an additional 10 points are added to your score.
• If the total is an odd number, 5 points are subtracted from your score.
• If you roll a double, you get to roll one extra die and get the number of points rolled added to your score.
• Your score cannot go below 0 at any point.
• The person with the highest score at the end of the 5 rounds wins.
• If both players have the same score at the end of the 5 rounds, 
    they each roll 1 die and whoever gets the highest score wins (this repeats until someone wins).


Click "Play" to continue
"""

def getDieValue():
    option = [1,2,3,4,5,6]
    number = random.choice(option)
    return number

def drawDie(c, x, y, val):
    
    c.create_rectangle(x, y, x+100, y+100)
    c.create_rectangle(x+4, y+4, x+96, y+96, fill="red", outline = '#8b0000')

    c.create_text(x+50,y+50,fill="white",font="Times 80 bold",
                            text=val)

def drawDice(c, yOfset, dice1X, dice2X, dice3X, dice4X, dice1, dice2, dice3, dice4):
    drawDie(c, dice1X, yOfset+100, dice1)
    drawDie(c, dice2X, yOfset+100, dice2)

    drawDie(c, dice3X, yOfset+100, dice3)
    drawDie(c, dice4X, yOfset+100, dice4)

def gameDisplay(width, yOfset, c, dice1, dice2, dice3, dice4):
    dice1X = width/2-350
    dice2X = width/2-200
    dice3X = width/2+100
    dice4X = width/2+250        
    c.create_text(dice1X+125,yOfset+50,fill="black",font="Times 40 bold",
                                text="{0}".format(player1))
    c.create_text(dice3X+125,yOfset+50,fill="black",font="Times 40 bold",
                                text="{0}".format(player2))

    c.create_text(dice1X+125,yOfset+250,fill="black",font="Times 40 bold",
                                text="Score: {0}".format(p1Score))
    c.create_text(dice3X+125,yOfset+250,fill="black",font="Times 40 bold",
                                text="Score: {0}".format(p2Score))
    drawDice(c, yOfset, dice1X, dice2X, dice3X, dice4X, dice1, dice2, dice3, dice4)


def drawGameCanvas(c, width, dice1, dice2, dice3, dice4):
    global rounds
    global btn
    c.delete("all")
    c.create_text(400,50,fill="black",font="Times 80 bold",
                                text="Dice Game")
    yOfset = 110

    gameDisplay(width, yOfset, c, dice1, dice2, dice3, dice4)

    # b = Button(window, text ="Hello", command = helloCallBack)
    # # b.place(x = width/2, y = yOfset + 250)
    # c.create_window(150, 100, window = b)
    if rounds < 0:
        btn = Button(c, text='Roll Sudden Death', font="Times 20 bold", width = 40, 
                    height=1, bd='10', command=rollDice)
    else:
        btn = Button(c, text='Roll', font="Times 20 bold", width = 40, 
                    height=1, bd='10', command=rollDice) 
    # btn.config(text="Roll")
    btn.place(x = 65, y = yOfset+290) 
    # btn.pack()

def add_score(playerName, score):
    global HighScores
    newScore = {"name": playerName, "score": score}
    HighScores.append(newScore)

def drawExitCanvas(c, width):
    global HighScores
    c.create_text(400,50,fill="black",font="Times 80 bold",
                                text="Dice Game")
    load = Image.open("Trophy.jpg")
    load = load.resize((100, 150), Image.ANTIALIAS)
    render = ImageTk.PhotoImage(load)
    img = Label(window, image=render)
    img.image = render
    img.place(x=350, y=150)



    yOfset = 110
    if p1Score > p2Score:
        c.create_text(400,350,fill="black",font="Times 40 bold",
                                text="{0} wins with a score of {1}".format(player1, p1Score))
    elif p2Score > p1Score:
        c.create_text(400,350,fill="black",font="Times 40 bold",
                                text="{0} wins with a score of {1}".format(player2, p2Score))
    else:
        c.create_text(400,350,fill="black",font="Times 40 bold",
                                text="Its a draw - Bonus Round Time")

    btn = Button(c, text='Quit', font="Times 20 bold", width = 40, 
                height=1, bd='10', command=exit)
    btn.place(x = 65, y = yOfset+290)


    filename = "HighScores.json"

    fi = open(filename, "r")
    High = fi.read()
    HighScores = json.loads(High)

    add_score(player1, p1Score)
    add_score(player2, p2Score)

    sorted_highscores = sorted(HighScores, key=lambda x: x["score"], reverse=True)
    highscoretable = sorted_highscores[:5]

    counter = 0
    yLev = 0*25+125
    c.create_text(720,yLev,fill="black",font="Times 20 bold",
                                    text="Highscores:")

    for player in highscoretable:
        global yLevel
        counter = counter + 1
        yLevel = counter*25+125
        c.create_text(720,yLevel,fill="black",font="Times 20 bold",
                                    text="{0} = {1}".format(player["name"], player["score"]))

    with open(filename, 'w') as outfile:
        json.dump(highscoretable, outfile)

def drawRulesCanvas(c, width):
    global rules
    c.create_text(400,50,fill="black",font="Times 80 bold",
                                text="Dice Game")
    yOfset = 110
    c.create_text(400,250,fill="black",font="Times 12 bold",
                            text="{0}".format(rules))
    
    btn = Button(c, text='Play', font="Times 20 bold", width = 40, 
                height=1, bd='10', command=lambda : startGame(btn))
    btn.place(x = 65, y = yOfset+290)

def startGame(btn):
    global c
    c.delete("all")
    btn.destroy()
    drawGameCanvas(c, width, "?", "?", "?", "?")

def testPlayer1Name(text, btn):
    dump(text)
    btn["state"] = NORMAL

def drawOpenCanvas(c, width):
    global rules
    global player1Name
    c.create_text(400,50,fill="black",font="Times 80 bold",
                                text="Dice Game")
    yOfset = 110

    entry1 = Entry(window, width = 20, font="Times 20 bold")
    c.create_window(400, 150, window=entry1)

    entry2 = Entry(window, width = 20, font="Times 20 bold")
    c.create_window(400, 225, window=entry2)

    c.create_text(150,150,fill="black",font="Times 20 bold",
                                text="Player 1 Name:")
    c.create_text(150,225,fill="black",font="Times 20 bold",
                                text="Player 2 Name:")
    text_id = c.create_text(400,325, fill="red",font="Times 30 bold",
                                text="")
    btn = Button(c, text='Continue', font="Times 20 bold", width = 40, 
                height=1, bd='10', command=lambda : showRules(entry1.get(), entry2.get(), btn, text_id))
    btn.place(x = 65, y = yOfset+290)
    # btn["state"] = DISABLED
    
    
def showRules(player1Name, player2Name, btn, text_id):
    autherized = ["Tom", "Dave", "Bob", "CPU", "Julie", "Holly"]
    global player1
    global player2
    # print(player1Name)
    if len(player1Name) == 0 or len(player2Name) == 0:
        c.itemconfig(text_id, text="Invalid Player Name")
        return
    
    if player1Name not in autherized or player2Name not in autherized:
        c.itemconfig(text_id, text="Unautherized Player Name")
        return

    player1 = player1Name
    player2 = player2Name
    c.delete("all")
    btn.destroy()
    drawRulesCanvas(c, width)
    
    

width = 800

window = Tk()
window.geometry("{0}x500".format(width))
window.title("Dice Game")
window.resizable(False, False)

# lbl = Label(window, text="Hello")
# lbl.grid(column=0, row=0)

c = Canvas(window, width=width, height=500, bg = '#afeeee')
c.pack()

rounds = 5
p1Score = 0
p2Score = 0

# player1Name = StringVar(window)

player1 = "Tom"
player2 = "CPU"

bonusRoll = 0

def normalRound():

    global rounds
    rounds = rounds - 1

    dice1 = getDieValue()
    dice2 = getDieValue()

    dice3 = getDieValue()
    dice4 = getDieValue()
    player1Score = dice1 + dice2
    player2Score = dice3 + dice4
    
    global p1Score
    global p2Score
    p1Score = p1Score + player1Score
    p2Score = p2Score + player2Score

    dump('{0} rolled a {1} and a {2}'.format(player1, dice1, dice2))
    dump('{0} rolled a {1} and a {2}'.format(player2, dice3, dice4))

    oddOrEven = player1Score % 2
    if oddOrEven == 1:
        # odd
        p1Score = p1Score - 5
    else:
        # even
        p1Score = p1Score + 10

    if p1Score < 0:
        p1Score = 0

    oddOrEven = player2Score % 2
    if oddOrEven == 1:
        # odd
        p2Score = p2Score - 5
    else:
        # even
        p2Score = p2Score + 10

    if p2Score < 0:
        p2Score = 0

    dump("{2}'s Score: {0}\t\t\t{3}'s Score: {1}".format(p1Score, p2Score, player1, player2))

    global bonusRoll

    if dice1 == dice2:
       bonusRoll = 1
    if dice3 == dice4:
      bonusRoll = bonusRoll + 2

    drawGameCanvas(c, width, dice1, dice2, dice3, dice4)

def suddenDeath():
    global p1Score
    global p2Score
    dice1 = getDieValue()
    dice3 = getDieValue()
    p1Score = p1Score + dice1
    p2Score = p2Score + dice3

    drawGameCanvas(c, width, dice1, "X", dice3, "X")

def bonusRollFunc():
    global bonusRoll
    global p1Score
    global p2Score
    dice1 = dice2 = dice3 = dice4 = "X"
    if bonusRoll == 1:
        dump('{0} has rolled a double, you get a bonus die'.format(player1))
        dice1 = getDieValue()
        p1Score = p1Score + dice1
    elif bonusRoll == 2:
        dump('{0} has rolled a double, you get a bonus die'.format(player2))
        dice3 = getDieValue()
        p2Score = p2Score + dice3
    else:
        dump('You both have rolled a double, you get a bonus role.')
        dice1 = getDieValue()
        dice3 = getDieValue()
        p1Score = p1Score + dice1
        p2Score = p2Score + dice3

    drawGameCanvas(c, width, dice1, dice2, dice3, dice4)
    
    bonusRoll = 0

def rollDice():
    global rounds
    global bonusRoll
    c.delete("all")
    btn.destroy()

    if bonusRoll == 0: 
        normalRound()
    else:
        bonusRollFunc()

    if rounds < 0:
        if p1Score == p2Score:
            suddenDeath()
        else:
            c.delete("all")
            btn.destroy()
            drawExitCanvas(c, width)

# drawRulesCanvas(c, width)
drawOpenCanvas(c, width)

window.mainloop()