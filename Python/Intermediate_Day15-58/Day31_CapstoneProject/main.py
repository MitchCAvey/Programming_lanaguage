from tkinter import *
from tkinter import messagebox
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
FILE_DIRECTORY = "./PersonalSource/Python/PythonBootCampt/Day31_CapstoneProject"
WORK_FILE_DIRECTORY = "./Python/PythonBootCampt/Day31_CapstoneProject"
ORIGIN_COUNTRY_FONT = 'Ariel'
ORIGIN_COUNTRY_FONT_SIZE = 40
current_card = {}

# ---------------------------- Button Functionality ------------------------------- #

try:
    data = pandas.read_csv(f"{FILE_DIRECTORY}/data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv(f"{FILE_DIRECTORY}/data/french_words.csv")
    words_to_learn = original_data.to_dict(orient="records")
else:
    words_to_learn = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(words_to_learn)
    # print(current_card["French"])
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=front_flash_card)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)

def is_known():
    words_to_learn.remove(current_card)
    data = pandas.DataFrame(words_to_learn)
    data.to_csv(f"{WORK_FILE_DIRECTORY}/data/words_to_learn.csv", index=False)


    next_card()
    

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(height=526, width=800)
front_flash_card = PhotoImage(file=f"{FILE_DIRECTORY}/images/card_front.png")
card_back_img = PhotoImage(file=f"{FILE_DIRECTORY}/images/card_back.png")
card_background = canvas.create_image(400, 263, image=front_flash_card)
card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)

# canvas.pack()
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
wrong_image = PhotoImage(file=f"{FILE_DIRECTORY}/images/wrong.png")
unknown_button = Button(image=wrong_image, command=next_card)
unknown_button.grid(row=1, column=0)

correct_image = PhotoImage(file=f"{FILE_DIRECTORY}/images/right.png")
known_button = Button(image=correct_image, command=is_known)
known_button.grid(row=1, column=1)

next_card()

window.mainloop()


