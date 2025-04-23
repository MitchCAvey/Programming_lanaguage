
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

# Different routes using the app.route decorator
@app.route("/bye")
def bye():
    return "Bye!"

# Creating variable paths and converting the path to a specified data type

@app.route("/username/<name>/<int:number>")
def greeting(name, number):
    return f"Hello there {name}, you are {number} years old!"

if __name__ == "__main__":
    # Run the app in debug mode to auto-reload
    app.run(debug=True)