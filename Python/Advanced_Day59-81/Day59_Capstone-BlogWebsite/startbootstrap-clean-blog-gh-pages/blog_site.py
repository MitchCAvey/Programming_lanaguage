

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/static/index.html")
def blog_site():
    return render_template('index.html')

@app.route("/static/about.html")
def about_page():
    return render_template('about.html')

@app.route("/static/contact.html")
def contact_page():
    return render_template('contact.html')

if __name__ == "__main__":
    # Run the app in debug mode to auto-reload
    app.run(debug=True)