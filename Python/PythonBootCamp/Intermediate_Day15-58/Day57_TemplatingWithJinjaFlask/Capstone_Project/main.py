from flask import Flask, render_template
from post import Post

post = ""
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", all_posts=post.get_all())

# @app.route('/post/<post_id>')


if __name__ == "__main__":
    post = Post()
    app.run(debug=True)
