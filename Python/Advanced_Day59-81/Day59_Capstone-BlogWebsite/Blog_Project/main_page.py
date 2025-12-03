

# from flask import Flask, render_template

# app = Flask(__name__)

# @app.route('/')
# def main_page():
#     # return render_template("index.html")
#     return render_template('index.html')

# if __name__ == "__main__":
#     app.run(debug=True)
    
    
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def blog_site():
    return render_template('index.html')

if __name__ == "__main__":
    # Run the app in debug mode to auto-reload
    app.run(debug=True)