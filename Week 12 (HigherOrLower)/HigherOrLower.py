# Author: Thomas Preston
import random

deck = {}

def addCards():
    for i in range(1, 14):
        cardValue = str(i)
        if i == 1: # Ace is Low
            cardValue = "A"
        if i == 11:
            cardValue = "J"
        if i == 12:
            cardValue = "Q"
        if i == 13:
            cardValue = "K"
        for suit in ["♤", "♧", "♡", "♢"]:
            deck[cardValue + suit]=i

def getShuffledDeck():
    shuffledDeck = list(deck.keys())
    random.shuffle(shuffledDeck)
    return shuffledDeck

addCards()
shuffled = getShuffledDeck()

print("Welcome to a game of Higher or Lower")
print("We're shuffling the deck")

card = shuffled.pop(0)

score = 0

while len(shuffled) > 0:
    valid = False
    guess=""   
    while(not valid):        
        guess = input("Is the next card higher [H] or lower [L] than the " + card + ": ").strip().upper()        
        if(len(guess) == 0):
            # print('empty')
            continue        
        if(len(guess) > 1):
            print('Too many letter entered')
            continue          
        if(not guess[0].isalpha()):                        
            print('Only enter letters')
            continue
        if(guess not in ["H", "L"]):
            print("Only the letters H/h and L/l are valid")
            continue
        valid = True

    nextCard = shuffled.pop(0)
    
    print("Next card:", nextCard)
    if deck[nextCard] == deck[card]:
        print("There the same - You loose")
        print('You had a final score of:', str(score))
        exit()
    elif deck[nextCard] > deck[card] and guess == "H":
        print("Higher - Well done")
        score = score + 1
        print("Score:", score)
    elif deck[nextCard] < deck[card] and guess == "L":
        print("Lower - Well done")
        score = score + 1
        print("Score:", score)
    else:
        print('Wrong - You loose')
        print('You had a final score of:', str(score))
        exit()
    card = nextCard