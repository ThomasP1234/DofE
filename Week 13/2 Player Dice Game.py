# Author: Thomas Preston

import random

authorisedPlayers = ["Tom", "John", "Bob", "Dave"]

def getAuthorisedPlayers():
    global player1
    player1 = input('Who is player one? ')
    global player2
    player2 = input('Who is player two? ')

    if player1 not in authorisedPlayers or player2 not in authorisedPlayers:
        print('Unauthorised to play')
        exit

dicePossibility = [1, 2, 3, 4, 5, 6]
p1Score = 0
p2Score = 0
rounds = 5

getAuthorisedPlayers()

print('The rules are:')
print('• The points rolled on each player’s dice are added to their score.')
print('• If the total is an even number, an additional 10 points are added to their score.')
print('• If the total is an odd number, 5 points are subtracted from their score.')
print('• If they roll a double, they get to roll one extra die and get the number of points rolled added to their score.')
print('• The score of a player cannot go below 0 at any point.')
print('• The person with the highest score at the end of the 5 rounds wins.')
print('• If both players have the same score at the end of the 5 rounds, they each roll 1 die and whoever gets the highest score wins (this repeats until someone wins).')

while rounds > 0:
    rounds = rounds - 1
    input('Press enter to roll the 2 dice each')

    player1dice1 = random.choice(dicePossibility)
    player1dice2 = random.choice(dicePossibility)
    player2dice1 = random.choice(dicePossibility)
    player2dice2 = random.choice(dicePossibility)

    # print(player1dice1, player1dice2, player2dice1, player2dice2)

    _player1Score = player1dice1 + player1dice2
    _player2Score = player2dice1 + player2dice2

    p1Score = p1Score + _player1Score
    p2Score = p2Score + _player2Score

    print('{0} rolled a {1} and a {2}'.format(player1, player1dice1, player1dice2))
    print('{0} rolled a {1} and a {2}'.format(player2, player2dice1, player2dice2))

    if player1dice1 == player1dice2:
        print('{0} has rolled a double, you get a bonus die'.format(player1))
        input('Press enter to roll')
        player1dice3 = random.choice(dicePossibility)
        print('You rolled a {0}, its been added straight to your score'.format(player1dice3))
        p1Score = p1Score + player1dice3
    if player2dice1 == player2dice2:
        print('{0} has rolled a double, you get a bonus die'.format(player2))
        input('Press enter to roll')
        player2dice3 = random.choice(dicePossibility)
        print('You rolled a {0}, its been added straight to your score'.format(player2dice3))
        p2Score = p2Score + player2dice3

    oddOrEven = _player1Score % 2
    if oddOrEven == 1:
        # odd
        p1Score = p1Score - 5
    else:
        # even
        p1Score = p1Score + 10

    if p1Score < 0:
        p1Score = 0

    oddOrEven = _player2Score % 2
    if oddOrEven == 1:
        # odd
        p2Score = p2Score - 5
    else:
        # even
        p2Score = p2Score + 10

    if p2Score < 0:
        p2Score = 0

    print("{2}'s Score: {0}\t\t\t{3}'s Score: {1}".format(p1Score, p2Score, player1, player2))

if p1Score > p2Score:
    print('{0} Wins'.format(player1))
elif p2Score > p1Score:
    print('{0} Wins'.format(player2))
else:
    print('Equal Score - Bonus Round')
    print('1 dice, highest wins')

    while True:
        input('Press enter to roll the 2 dice each')

        player1dice1 = random.choice(dicePossibility)
        player2dice1 = random.choice(dicePossibility)

        print('{0} rolled a {1} and a {2}'.format(player1, player1dice1, player1dice2))
        print('{0} rolled a {1} and a {2}'.format(player2, player2dice1, player2dice2))

        if player1dice1 > player2dice1:
            print('{0} Wins'.format(player1))
            break
        elif player2dice1 > player1dice1:
            print('{0} Wins'.format(player2))
            break
        else:
            print('Equal - redo')
            continue