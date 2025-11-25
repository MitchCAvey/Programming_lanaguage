from tkinter import *
import requests

"""
NOTE: This API only works on my personal PC's
"""

FILE_DIRECTORY = "./PersonalSource/Python/PythonBootCampt/Day33_API-Endpoints/KanyeQuoteProject"
WORK_FILE_DIRECTORY = "./Python/PythonBootCampt/Day33_API-Endpoints/KanyeQuoteProject"

def get_quote():

    response = requests.get(url="https://api.kanye.rest")
    response.raise_for_status()
    data = response.json()
    # print(data)
    qoute = data['quote']
    canvas.itemconfig(quote_text, text=qoute)
    #Write your code here.



window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file=f"{WORK_FILE_DIRECTORY}/background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file=f"{WORK_FILE_DIRECTORY}/kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)



window.mainloop()