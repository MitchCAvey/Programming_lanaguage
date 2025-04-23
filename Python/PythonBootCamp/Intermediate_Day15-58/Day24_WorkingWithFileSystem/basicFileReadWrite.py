

# Details how to open and read a file.
with open("./Day24_WorkingWithFileSystem/my_file.txt") as file:
# file = open("my_file.txt")

    contents = file.read()

    print(contents)

# file.close()

with open("./Day24_WorkingWithFileSystem/my_file.txt", mode="a") as file:
    file.write("\nAdding new text to the file")