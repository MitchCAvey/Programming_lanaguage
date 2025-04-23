
from flask import Flask

app = Flask(__name__)

# print(__name__)

@app.route("/")
def hello_world():
    return "Hello, World!"

@app.route("/bye")
def say_bye():
    return "Bye"

# @app.route("/username/<name>")
# @app.route("/<name>")
# @app.route("/<username>")
# @app.route("/<name>")
# @app.route("/username/<name>/1")
@app.route("/username/<path:name>")
# @app.route("/username/<name>/<int:number>")
def greet(name):
# def greet(name, number):
    return f"Hello there {name}"
    # return f"Hello there {name + '86'}, you are {number} old"

if __name__ == "__main__":
    app.run(debug=True) 


# # Basic code to run some HTML code in Flask
# from flask import Flask

# app = Flask(__name__)

# @app.route("/")
# def hello_world():
#     return '<h1 style="text-align: center">Hello, World!</h1>' \
#         '<p>This is paragraph</p>' \
#             '<img src="https://images.unsplash.com/photo-1529778873920-4da4926a72c2?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8N3x8a2l0dGVufGVufDB8fDB8fHww?"width=200>' \
#                 '<br>' \
#                     '<img src=https://media1.giphy.com/media/1BXa2alBjrCXC/giphy.webp?cid=82a1493bjfxqlkp0tsntjfveaw7838ig9wtzqbxmf3whr8y5&ep=v1_gifs_trending&rid=giphy.webp&ct=g>'

# @app.route("/bye")
# def bye():
#     return "<p>Bye from Mars!</p>"

# @app.route("/username/<name>")
# def greet(name):
#     return f"Hello my friend {name}"

# if __name__ == "__main__":
#     app.run(debug=True)


# ## Advanced Python Decorator Functions

# class User:
#     def __init__(self, name):
#         self.name = name
#         self.is_logged_in = False

# def is_authenticated_decorator(function):
#     def wrapper(*args, **kwkargs):
#         if args[0].is_logged_in == True:
#             function(args[0])
#     return wrapper

# @is_authenticated_decorator
# def create_blog_post(user):
#     print(f"This is {user.name}'s new blog post.")

# new_user = User("Mic")
# new_user.is_logged_in = True # Setting is_logged_in to True
# create_blog_post(new_user)
