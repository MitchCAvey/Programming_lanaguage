"""
These are the four keywords to handling errors in Python

try: Something that might cause an exception
except: do this if there was an exception
else: Do this if there were no exceptions
finally: Do this no matter what happens

"""

# This generates the FileNotFound error
# with open("random_file.txt") as file:
#     file.read()

# try:
#     file = open("random_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary("alsk;fal"))
# except FileNotFoundError:
#     # print("There was an error")
#     file = open("random_file.txt", "w")
#     file.write("Something after handling the error")
# except KeyError as error_message:
#     print(f"The key {error_message} doesn't exist!")
# else: 
#     content = file.read("random_file.txt")
# finally:
#     # file.close("random_file.txt")
#     # print("File was closed")
#     raise KeyError(" This is just to deminstrate rasing your own error's ")

# height = float(input("Height: "))
# weight = int(input("Weight: "))

# if height > 3:
#     raise ValueError("Your height value is to large. Normal human height is 3 meters max")

# bmi = weight / height ** 2

# print(bmi)

# Convert formatted string to list
# fruits = eval(input())

# print(fruits)

# # Catch the exception and make sure the code runs without crashing.
# def make_pie(index):
#   try:
#     fruit = fruits[index]
#   except IndexError:
#     print("Fruit pie")
#   else:
#     print(fruit + " pie")

# try:
#     user_selection = int(input("Enter selection here:"))
#     make_pie(user_selection) # Raises IndexError on list with less than 5 items.
# except ValueError:
#     print("Please enter a number value")
#     user_selection = int(input("Enter selection here:"))
#     make_pie(user_selection) # Raises IndexError on list with less than 5 items.


# eval() function will create a list of dictionaries using the input
# Note: when entering the values at the prompt, make sure to include the 
# datatype's format when manual creating, e.g. ["Apple", "Pear", "Cherry"] or "Some text here", etc.
facebook_posts = eval(input())

total_likes = 0
# TODO: Catch the KeyError exception

# try:
for post in facebook_posts:
    try:
        total_likes = total_likes + post['Likes']
    except KeyError:
        # total_likes += 0
        # continue
        pass

print(total_likes)

  


# This generates the KeyError
# a_dictionary = {"key": "value"}
# value = a_dictionary["non_existent_key"]

# This generates the IndexError
# fruit_list = ["Apple", "Banana", "Pear"]
# fruit = fruit_list[3]

# TypeError
# text = "abc"
# print(text + 5)


