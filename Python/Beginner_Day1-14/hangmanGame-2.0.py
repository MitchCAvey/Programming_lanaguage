import random

#Step 1 
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["ardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(f"The word that has been selected is: {chosen_word}")

display = []
for length in range(0, len(chosen_word)):
    #pass
    display.append('_')

end_of_game = False

lives = 6

while not end_of_game:
    guess = input("Enter your letter guess here: ").lower()

    for position in range(0, len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            #print(f"Right!")
            display[position] = letter
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You Lose!")
    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True

    print(stages[lives])