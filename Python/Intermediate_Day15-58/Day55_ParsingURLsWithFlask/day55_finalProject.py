

from flask import Flask
import random

app = Flask(__name__)

ran_num = random.randint(0, 9)
print(ran_num)

@app.route("/")
def home_page():
    return '<h1>Guess a number between 0 and 9</h1>' \
        '<img src="https://media0.giphy.com/media/A8OSeenhtpey43CcMG/200.webp?cid=ecf05e47vhx6672f19l6a7kad70a37blwiyheah7j5ym0h79&ep=v1_gifs_search&rid=200.webp&ct=g">'

@app.route("/<int:num_guess>")
def guessing_number(num_guess):
    if num_guess > ran_num:
        return "<h1 style='color: purple'>Too high, try again!</h1>" \
            "<img src='https://media4.giphy.com/media/YKroe55zFMIwpmBCu6/giphy.webp?cid=790b7611wzhv6xl2t0ywkmdlfy1y6s2tjhs86r590cpron8g&ep=v1_gifs_search&rid=giphy.webp&ct=g'>"
    elif num_guess < ran_num:
        return "<h1 style='color: red'>Too Low, try again!</h1>" \
            "<img src='https://media1.giphy.com/media/QdBqnfDfalVps2XvB9/200.webp?cid=ecf05e47xydu5owxkfalexka8lutiufybuxaqdsei9tcazc1&ep=v1_gifs_search&rid=200.webp&ct=g'>"
    else:
        return "<h1 style='color: green'>Guess what!</h1>" \
            "<img src='https://media3.giphy.com/media/DFu7j1d1AQbaE/giphy.webp?cid=790b7611kvjlyh5l1wa8ikexz03nfxq86zfxpuqah1v4kdv7&ep=v1_gifs_search&rid=giphy.webp&ct=g'>"

if __name__ == "__main__":
    # Run the app in debug mode to auto-reload
    app.run(debug=True)