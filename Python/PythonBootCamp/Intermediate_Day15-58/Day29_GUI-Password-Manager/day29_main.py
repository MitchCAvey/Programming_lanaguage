from tkinter import *
from random import *
from tkinter import messagebox
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 
            'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 
            'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 
            'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    passwd_letters = [choice(letters) for _ in range(randint(8, 10))]
    passwd_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    passwd_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = passwd_letters + passwd_numbers + passwd_symbols
    
    shuffle(password_list)
    # print(password_list)

    # passwd = ''
    # for char in password_list:
    #     passwd += char
    
    passwd = ''.join(password_list)
    pyperclip.copy(passwd)
    
    # print(passwd)

    passwd_entry.insert(0, passwd)



# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_entry.get()
    email = email_username_entry.get()
    passwd = passwd_entry.get()

    if len(website) == 0 or len(passwd) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty")
    else:
        # messagebox.showinfo(title="title", message="message")
        is_ok = messagebox.askokcancel(title="title", message=f"These are the details entered: \nEmail: {email}\nPassword: {passwd}")

        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {passwd}\n")
                website_entry.delete(0, END)
                passwd_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

# Builds the basic window
window = Tk()
window.title("MyPass")
window.config(padx=50, pady=50)

# Creates the "canvas" that allows you to place images, widgets, etc.
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="./logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)
# canvas.pack()

# Labels
website_label = Label(text="Website: ")
website_label.grid(row=1, column=0)
email_username_label = Label(text="Email/Username : ")
email_username_label.grid(row=2, column=0)
passwd_label = Label(text="Password : ")
passwd_label.grid(row=3, column=0)


# Entries
website_entry = Entry(width=55)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_username_entry = Entry(width=55)
email_username_entry.grid(row=2, column=1, columnspan=2)
email_username_entry.insert(0, "Bugs.Bunny@acmeinc.com")
passwd_entry = Entry(width=35)
passwd_entry.grid(row=3, column=1)

# Buttons
generate_passwd_button = Button(text="Generate Passworde", command=generate_password)
generate_passwd_button.grid(row=3, column=2)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()