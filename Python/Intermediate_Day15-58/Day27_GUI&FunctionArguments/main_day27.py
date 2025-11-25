
# import tkinter

# # Basic code to setup a bare-bones GUI window 
# window = tkinter.Tk()
# window.title("My First GUI Program")
# window.minsize(width=500, height=300)

# # Creating a Label
# my_label = tkinter.Label(text="My first Label", font=("Arial", 20, "bold"))
# my_label.pack(side="left")

# # my_label["text"] = "New Text"
# # my_label.config(text="New Text 2")

# # Creating buttons
# button = tkinter.Button


# window.mainloop()

# This allows us to import all the class within tkinter
from tkinter import *

# Basic code to setup a bare-bones GUI window 
window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# Creating a Label
my_label = Label(text="My first Label", font=("Arial", 20, "bold"))
# my_label.pack(side="left")
my_label.pack()

# my_label["text"] = "New Text"
# my_label.config(text="New Text 2")

# Creating a action when a button is clicked
def button_clicked():
    print("I was clicked!")
    new_text = input.get()
    my_label.config(text=new_text)

# Creating buttons
button = Button(text="Click Me", command=button_clicked)
button.pack()

# Entry
input = Entry(width=50)
input.pack()
input.get()



window.mainloop()

