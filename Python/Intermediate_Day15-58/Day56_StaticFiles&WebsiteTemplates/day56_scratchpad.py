
# Basic code to run some HTML code in Flask
from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def main_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)


"""
Use this JavaScript code in the browsers Console in Development Tools:

document.body.contentEditable=true
"""