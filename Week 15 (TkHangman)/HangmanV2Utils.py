# HangmanV2
# Author: Thomas Preston

import random

# def selectPuzzle():
f = open("Hangmanlist.txt", "r")
answer_str = f.read()
answer_list = answer_str.split(',')
answer = random.choice(answer_list)
answer_uppercase = answer.upper()

solution_letters = ""
for letter in answer_uppercase:        
    if(letter != " " and letter not in solution_letters):
        solution_letters += letter
solution_letter_count = len(solution_letters)


valid_letters = []
invalid_letters = []

def getPuzzleString():
    puzzle=""
    for letter in answer_uppercase:
        if(letter == " " or letter in valid_letters):
            puzzle += letter        
        else:
            puzzle += "_"
    return puzzle

def processGuess(guess):
    state = 0
    if(guess in answer_uppercase):
        # print("Yes {0} is in the puzzle.".format(guess))
        valid_letters.append(guess)        
        state = 1
        if(solution_letter_count == len(valid_letters)):
            # print("Game over - You win -- well done!")
            state = 3
    else:            
        # print("No {0} is not in the puzzle".format(guess))
        invalid_letters.append(guess)
        state = 2
    
    return state

def getStatus():
    return len(invalid_letters)