import random

EASYLEVELTRIES = 10
HARDLEVELTRIES = 5 

def generateRandNum():
    return random.randint(1, 101)

def difficultyChoice(number):
    choice = ""
    print("I'm thinking of a number between 1 and 100.")
    print(f"pssst, the correct answer is {number}")
    choice = input("Choose a difficulty. Type 'easy' or 'hard':").lower()
    return choice

def setUpGame():
    numberToGuess = generateRandNum()
    difficulty = difficultyChoice(numberToGuess)
    if difficulty == "easy":
        playerGuess(EASYLEVELTRIES, numberToGuess)
    elif difficulty == "hard":
        playerGuess(HARDLEVELTRIES, numberToGuess)

def playerGuess(totalTries, randNumToGuess):
    tries = int(totalTries)
    playerWins = False
    numToGuess = int(randNumToGuess)
    while tries != 0 and not playerWins:
        print(f"You have {tries} attempts remaining to guess the number.")
        choose = int(input("Make a guess: "))
        if choose < numToGuess:
            print("Too Low.")
            tries -= 1
            if tries != 0:
                print("Guess again.")
        elif choose > numToGuess:
            print("Too High.")
            tries -= 1
            if tries != 0:
                print("Guess again.")
        else:
            print(f"You got it! The answer was {numToGuess}")
            playerWins = True
    if tries == 0:
        print("You've run out of guesses, you lose.")

setUpGame()