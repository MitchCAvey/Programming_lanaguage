#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 
           'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 
           'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 
           'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
passwd = ''
totalPW_length = nr_letters + nr_symbols + nr_numbers

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

# Instructors version
passwd_list = []
for char in range(0, nr_letters):
    passwd_list.append(random.choice(letters))

for symbol in range(0, nr_symbols):
    passwd_list.append(random.choice(symbols))

for number in range(0, nr_numbers):
    passwd_list.append(random.choice(numbers))

random.shuffle(passwd_list)

passwd2 = ''

for char in passwd_list:
	passwd2 += char

print(f"Password = {passwd2}")


"""
for num in range(totalPW_length):
    randnum = random.randint(1, 3)
    if randnum == 1:
        randomNum = random.randrange(0, len(letters))
        passwd += str(letters[randomNum])
    elif randnum == 2:
        randomNum = random.randrange(0, len(symbols))
        passwd += symbols[randomNum]
    elif randnum == 3:
        randomNum = random.randrange(0, len(numbers))
        passwd += numbers[randomNum]

print(f"Password = {passwd}")
"""

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

"""
passwd = ''

for char in range(0, nr_letters):
    passwd += random.choice(letters)

for char in range(0, nr_symbols):
    passwd += random.choice(symbols)

for char in range(0, nr_numbers):
    passwd += random.choice(numbers)

print(f"Total Length of password is: {totalPW_length}")
counter = 0

for n in range(nr_letters):
    randomNum = random.randrange(0, len(letters))
    #print(f"Random Numbers based on number of Letters: {randomNum}")
    print(f"This is the letter for based on the random number: {letters[randomNum]}")
    passwd += str(letters[randomNum])

print(f"Password after first for loop = {passwd}")

for n in range(nr_symbols):
    randomNum = random.randrange(0, len(symbols))
    #print(f"Random Numbers based on number of Letters: {randomNum}")
    print(f"This is the letter for based on the random number: {symbols[randomNum]}")
    passwd += symbols[randomNum]

print(f"Password after second for loop = {passwd}")

for n in range(nr_numbers):
    randomNum = random.randrange(0, len(numbers))
    #print(f"Random Numbers based on number of Letters: {randomNum}")
    print(f"This is the letter for based on the random number: {numbers[randomNum]}")
    passwd += numbers[randomNum]

    
print(f"Password after second for loop = {passwd}")
"""