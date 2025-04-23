

# TODO: Create the logging_decorator() function 👇
# def logging_decorator(a_function):
#     def wrapper_function(*args):
#         print(f"You called {a_function.__name__}{args}")
#         results = a_function(*args)
#         print(f"It returned: {results}")
#         return results
#     return wrapper_function

def logging_decorator(func):
    def wrapper(*args):
        print(f"You called {func.__name__}{args}")
        result = func(*args)
        print(f"It returned: {result}")
        return result
    return wrapper

# TODO: Use the decorator 👇
@logging_decorator
def a_function(*args):
    return sum(args)
    
a_function(1,2,3)
