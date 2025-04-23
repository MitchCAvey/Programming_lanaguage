
import random
from gameData import data
from art import vsLogo
from art import gameLogo

def generateRandomNumber():
    return random.randint(0, len(data))

def pickOpponents():
    selectedOpponents = []
    opponentANum = generateRandomNumber()
    opponentBNum = generateRandomNumber()

    if opponentANum == opponentBNum:
        opponentBNum = generateRandomNumber()

    selectedOpponents.append(data[opponentANum - 1])
    selectedOpponents.append(data[opponentBNum - 1])
    
    return selectedOpponents

def setupMatch():
    opponentList = pickOpponents()
    winning = True
    score = 0

    while winning:
        print(f"Opponent A's: {opponentList[0]['name']}; Description: {opponentList[0]['description']}; Country: {opponentList[0]['country']}; FollowerCount: {opponentList[0]['follower_count']}")
        print(f"{vsLogo}")
        print(f"Opponent B's: {opponentList[1]['name']}; Description: {opponentList[1]['description']}; Country: {opponentList[1]['country']}; FollowerCount: {opponentList[1]['follower_count']}")
        answer = input("Who has more follwers? Type 'A' or 'B' :").upper()
        if opponentList[0]['follower_count'] > opponentList[1]['follower_count']:
            if answer == 'A':
                print("You Win this Round!")
                opponentList = pickOpponents()
                score += 1
            else:
                print("You Lost this round!")
                winning = False
        elif opponentList[1]['follower_count'] > opponentList[0]['follower_count']:
            if answer == 'B':
                print("You Win this Round!")
                opponentList = pickOpponents()
                score += 1
            else:
                print("You Lost this round!")
                winning = False
        print(f"Your Final Score is: {score}")

setupMatch()




