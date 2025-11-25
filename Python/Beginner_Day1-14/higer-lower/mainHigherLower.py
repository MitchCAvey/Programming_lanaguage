
import random
from gameData import data
from art import vsLogo
from art import gameLogo

def generateRandomNumber():
    return random.randint(0, len(data) + 1)

# def pickOpponentA():
#     randIndexNum = int(generateRandomNumber())
#     return data[randIndexNum]

# def pickOpponentB():
#     randIndexNum = int(generateRandomNumber())
#     #if data[randIndexNum] 
#     return data[randIndexNum]

# def pickOpponent():
#     selectedOpponents = []
#     randomNumberA = int(generateRandomNumber())
#     randomNumberB = int(generateRandomNumber())
#     if randomNumberA == randomNumberB:
#         randomNumberB = int(generateRandomNumber())
#     else:
#         selectedOpponents.append(data[randomNumberA])
#         selectedOpponents.append(data[randomNumberB])
#     return selectedOpponents

def pickOpponents():
    selectedOpponents = []
    # selectedOpponents.append(data[int(generateRandomNumber())])
    # print(len(selectedOpponents))
    while len(selectedOpponents) < 2:
        selectedOpponents.append(data[generateRandomNumber()])
    #print(selectedOpponents)
    return selectedOpponents

# def pickOpponents():
#     selectedOpponents = []
#     currntRandNum = int(generateRandomNumber())

#     while len(selectedOpponents) < 2:
#         selectedOpponents.append(data[currntRandNum])
#     return selectedOpponents


def setupMatch():
    #print(f"{pickOpponent()}")
    opponentList = pickOpponents()
    #print(f"{opponentList}")
    winning = True
    while winning:
        print(f"Opponent A's: {opponentList[0]['name']}; Description: {opponentList[0]['description']}; Country: {opponentList[0]['country']}; FollowerCount: {opponentList[0]['follower_count']}")
        print(f"{vsLogo}")
        print(f"Opponent B's: {opponentList[1]['name']}; Description: {opponentList[1]['description']}; Country: {opponentList[1]['country']}; FollowerCount: {opponentList[1]['follower_count']}")
        answer = input("Who has more follwers? Type 'A' or 'B' :").upper()
        if opponentList[0]['follower_count'] > opponentList[1]['follower_count']:
            if answer == 'A':
                print("You Win this Round!")
                opponentList = pickOpponents()
                #opponentList[0] = opponentList[1]
                #opponentList[1] = data[int(generateRandomNumber())]
            else:
                print("You Lost this round!")
                winning = False
        elif opponentList[1]['follower_count'] > opponentList[0]['follower_count']:
            if answer == 'B':
                print("You Win this Round!")
                opponentList = pickOpponents()
                #opponentList[0] = opponentList[1]
                #opponentList[1] = data[int(generateRandomNumber())]
            else:
                print("You Lost this round!")
                winning = False

setupMatch()
#pickOpponent()

# def setupMatch():
#     print(f"{gameLogo}")
#     opponentA = pickOpponentA()
#     opponentB = pickOpponentB()
#     print(f"Opponent A's: {opponentA['name']}; Description: {opponentA['description']}; Country: {opponentA['country']}; FollowerCount: {opponentA['follower_count']}")
#     print(f"{vsLogo}")
#     print(f"Opponent B's: {opponentB['name']}; Description: {opponentB['description']}; Country: {opponentB['country']}; FollowerCount: {opponentB['follower_count']}")
#     answer = input("Who has more follwers? Type 'A' or 'B' :").upper()
#     if answer == 'A':
#         if opponentA['follower_count'] > opponentB['follower_count']:
#             print("You've Won this Round!!")
#         else:
#             print("You've lost this round!!")
#         #playgame(answer, opponentA, opponentB)
#     else:
#         if opponentB['follower_count'] > opponentA['follower_count']:
#             print("You've Won this Round!!")
#         else:
#             print("You've lost this round!!")


# The below is my idea's and or failed idea's
"""
def setupMatch():
    #print(f"{pickOpponent()}")
    opponentList = pickOpponent()
    #print(f"{opponentList}")
    winning = True
    while winning:
        for num in range(0, len(opponentList)):
            if num == 0:
                print(f"Opponent A's: {opponentList[num]['name']}; Description: {opponentList[num]['description']}; Country: {opponentList[num]['country']}; FollowerCount: {opponentList[num]['follower_count']}")
            else:
                print(f"{vsLogo}")
                print(f"Opponent B's: {opponentList[num]['name']}; Description: {opponentList[num]['description']}; Country: {opponentList[num]['country']}; FollowerCount: {opponentList[num]['follower_count']}")
            answer = input("Who has more follwers? Type 'A' or 'B' :").upper()
            if opponentList[0]['follower_count'] > opponentList[1]['follower_count']:
                if answer == 'A':
                    print("You Win this Round!")
                    opponentList = pickOpponent()
                    #opponentList[0] = opponentList[1]
                    #opponentList[1] = data[int(generateRandomNumber())]
                else:
                    print("You Lost this round!")
                    winning = False
            elif opponentList[1]['follower_count'] > opponentList[0]['follower_count']:
                if answer == 'B':
                    print("You Win this Round!")
                    opponentList = pickOpponent()
                    #opponentList[0] = opponentList[1]
                    #opponentList[1] = data[int(generateRandomNumber())]
                else:
                    print("You Lost this round!")
                    winning = False

def pickOpponent():
    selectedOpponents = []
    for num in range(0,2):
        selectedOpponents.append(data[int(generateRandomNumber())])
        print(selectedOpponents)
        if len(selectedOpponents) == 1:
            return selectedOpponents


    currentOpponentA = pickOpponentA()
    if data[randIndexNum] != currentOpponentA:
        return data[randIndexNum]
    else:
        pickOpponentB()

def pickOpponent():
    selectedOpponents = []
    randomNumberA = int(generateRandomNumber())
    randomNumberB = int(generateRandomNumber())
    if randomNumberA == randomNumberB:
        randomNumberB = int(generateRandomNumber())



def playgame(playersAnswer, opponentA, opponentB):
    print(f"Players Answer: {playersAnswer}")
    print(f"Opponent A Details: {opponentA}")
    print(f"Opponent B Details: {opponentB}")

"""



