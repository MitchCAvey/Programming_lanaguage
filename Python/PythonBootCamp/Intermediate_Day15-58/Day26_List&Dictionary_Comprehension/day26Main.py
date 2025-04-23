import math

FILE_DIRECTORY = "./PersonalSource/Python/PythonBootCampt/Day26_List&Dictionary_Comprehension"
WORK_FILE_DIRECTORY = "./Python/PythonBootCampt/Day26_List&Dictionary_Comprehension"

# Basics of creating a new list, where each number in the list is increased by 1
# numbers = [1,2,3]
# new_list = []
# for n in numbers:
#     add_1 = n + 1
#     new_list.append(add_1)

# print(f"From the numbers list: {numbers}")
# print(f"From the new_list list: {new_list}")

# List Comprehension basic structure
#new_list1 = [new_list1 for item in list]
# new_list1 = [n + 1 for n in numbers]

# print(f"new_list1 using list comprehension {new_list1}")


# name = "Mitchell"

# new_list2 = [letter for letter in name]
# print(new_list2)

#range(1,5)

# new_list3 = [num * 2 for num in range(1,5)]
# print(new_list3)

# Conditional List Comprehension
#new_list = [new_item for item in list if test]

# name_list = ["Logan", "Jen", "Scott", "Remi", "Hank", "Charles"]
# new_list4 = [name for name in name_list if len(name) < 5]
# print(new_list4)

# new_list5 = [name.upper() for name in name_list if len(name) >= 5]
# print(new_list5)

# numbers1 = [1,1,2,3,5,8,13,21,34,55]

# square_numbers = [pow(num, 2) for num in numbers1]

# print(square_numbers)

# list_of_strings = input().split(',')

# numbers = [int(x) for x in list_of_strings]

# result= [num for num in numbers if num % 2 == 0]

# print(result)


# with open(f"{WORK_FILE_DIRECTORY}/file1.txt") as file1:
#   list1 = file1.readlines()
# with open(f"{WORK_FILE_DIRECTORY}/file2.txt") as file2:
#   list2 = file2.readlines()

# result = [int(num) for num in list1 if num in list2]
# result = [num.strip() for num in list1 if num in list2]

# Write your code above 
# print(result)


import random

student_names = ["Logan", "Jen", "Scott", "Remi", "Hank", "Charles"]

# Basic syntax: student_score = {new_key:new_value for item in list}
student_score = {student:random.randint(1,100) for student in student_names}

print(student_score)

passed_students = {student:score for (student, score) in student_score.items() if score >= 60}

print(passed_students)


import pandas
student_dict = {
   "student": ["Angela", "James", "Lily"],
   "score": [56, 76, 98]
}

# Looping through dictionaries:
# for (key, value) in student_dict.items():
#    print(key)
#    print(value)

# student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)

# Loop through a data frame
# for (key, value) in student_data_frame.items():
#    print(key)
#    print(value)

# Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#    print(index)
#    print(row)

# for (index, row) in student_data_frame.iterrows():
#    if row.student == "Angela":
#       print(row.student)
#       print(row.score)


