# Hangman game
# Author: Thomas Preston

import random
answer_list = ["The Hobbit","The Wizard of Oz","Iron Man"]
answer = random.choice(answer_list)
#answer = "The Hobbit"
lives = 4

answer_uppercase = answer.upper()
solution_letters = ""
for letter in answer_uppercase:        
    if(letter != " " and letter not in solution_letters):
        solution_letters += letter
solution_letter_count = len(solution_letters)
print(solution_letters, solution_letter_count)

valid_letters = []
invalid_letters = []

print("Welcome to Hangman!")
end=False
while(not end):
    puzzle=""
    for letter in answer_uppercase:
        if(letter == " " or letter in valid_letters):
            puzzle += letter        
        else:
            puzzle += "-"
    print(puzzle)

    print("Bad Guesses: ", invalid_letters, "\tLives: ", lives-len(invalid_letters))

    valid = False
    guess=""
    print('Enter a letter as your guess:')    
    while(not valid):        
        valid = True
        guess = input().strip().upper()        
        if(len(guess) == 0):
            # print('empty')
            continue        
        if(len(guess) > 1):
            print('Too many letter entered')
            continue          
        if(not guess[0].isalpha()):                        
            print('Only enter letters')
            continue
        valid = True
   
    if(guess in answer_uppercase):
        print("Yes {0} is in the puzzle.".format(guess))
        valid_letters.append(guess)            
        if(solution_letter_count == len(valid_letters)):
            print("Game over - You win -- well done!")
            end=True
    else:            
        print("No {0} is not in the puzzle".format(guess))
        invalid_letters.append(guess)

    if(len(invalid_letters) >= lives):
        print("Game Over -- You loose -- Hang Um High!!")
        end=True
   
print("The answer was: {0}".format(answer))