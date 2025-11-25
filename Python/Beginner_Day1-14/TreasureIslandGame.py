
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#Write your code below this line

print("You've come to a fork in the road, with one path leading right the other leading left")
choice1 = input("Which path do you take? Type \"left\" or \"right\": ")

if choice1 == 'left':
    print("You walk for some time and come upon a lake, which has a lake in the middle of it")
    print("You can either wait for the boat, or you can swim?")
    choice2 = input(" Type \"wait\" for the boat or type \"swim\" to swim to the island: ")
    if choice2 == 'wait':
        print("The takes you a small dock on the Island, and points to Red, Yellow, & Blue doors")
        print("And says, Pick one")
        choice3 = input("Type \"red\", \"yellow\", or \"blue\" for the door you've picked: ")
        if choice3 == 'yellow':
            print("You've Found the Teasure")
        else:
            print("GAME OVER!")
    else:
        print("GAME OVER!")        
else:
    print("GAME OVER!")