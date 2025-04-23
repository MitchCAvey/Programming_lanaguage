
# # Basic code to run some HTML code in Flask
# from flask import Flask

# app = Flask(__name__)

# # print(__name__)

# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"

# if __name__ == "__main__":
#     app.run()



# # Functions inputs/functionality/output

# def add(n1, n2):
#     return n1 + n2

# def subtract(n1, n2):
#     return n1 - n2

# def multiply(n1, n2):
#     return n1 * n2

# def divide(n1, n2):
#     return n1 / n2

# # Functions are First-class objects, can be passed around as arguments e.g.
# # int/string/float etc.

# def calculate(calc_function, n1, n2):
#     return calc_function(n1, n2)

# result = calculate(add, 2, 3)
# print(result)

# result = calculate(subtract, 2, 3)
# print(result)

# result = calculate(multiply, 2, 3)
# print(result)

# result = calculate(divide, 2, 3)
# print(result)


# # Nested functions

# def outer_function():
#     print("I'm outer")
    
#     def nested_function():
#         print("I'm Inner")
    
#     nested_function()

# outer_function()

# # Functions can be returned from other functions

# def outer_function():
#     print("I'm outer")
    
#     def nested_function():
#         print("I'm Inner")
    
#     return nested_function # returning functions don't need the '()'

# inner_function = outer_function()

# inner_function()

# ## Python Decorator Function


# def decorator_function(function):
#     """This is a basic example of how a decorator function is setup  """
#     def wrapper_function():
#         function()
#     return wrapper_function

# import time

# def decorator_function(function):
#     """This is a basic example of how a decorator function is setup  """
#     def wrapper_function():
#         function()
#     return wrapper_function

# def say_hello():
#     # time.sleep(2)
#     print(f"Hello")

# def say_bye():
#     print(f"Good Bye")

# def say_greeting():
#     print(f"How are you today old chap?")

# import time

# def delay_decorator(function):
#     """This is a basic example of how a decorator function is setup  """
#     def wrapper_function():
#         time.sleep(2)
#         # Do something before
#         function()
#         # Do something after
#     return wrapper_function

# @delay_decorator # This function will have the delay found in the wrapper function
# def say_hello():
#     print(f"Hello")

# @delay_decorator # This function will have the delay 
# def say_bye():
#     print(f"Good Bye")

# def say_greeting(): # This function will not have the delay
#     print(f"How are you today old chap?")

# # say_hello()
# # say_greeting()
# # say_bye()

# # Lets say that you want to add the say_greeting function to use the delay_decorator function
# # You would do the following:
# say_hello()
# decorated_greeting_function = delay_decorator(say_greeting)
# decorated_greeting_function()
# say_bye()


# Basic code to run some HTML code in Flask
from flask import Flask

app = Flask(__name__)

# print(__name__)

@app.route("/")
def hello_world():
    return "Hello, World!"

@app.route("/bye")
def say_bye():
    return "Bye"

if __name__ == "__main__":
    app.run()



# import time

# current_time = time.time()
# print(current_time)  # seconds since Jan 1st, 1970


# # Write your code below 👇

# def speed_calc_decorator(function):
#     def wrapper():
#         start_time = time.time()
#         result = function()
#         end_time = time.time()
#         print(f"{function.__name__} run speed: {end_time - start_time}s")
#         return result

#     return wrapper


# @speed_calc_decorator
# def fast_function():
#     for i in range(1000000):
#         i * i


# @speed_calc_decorator
# def slow_function():
#     for i in range(10000000):
#         i * i