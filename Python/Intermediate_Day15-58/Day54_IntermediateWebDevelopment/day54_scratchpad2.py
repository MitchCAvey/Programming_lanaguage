

import time
current_time = time.time()
print(current_time) # seconds since Jan 1st, 1970 

# Write your code below 👇

def speed_calc_decorator(function):
    def wrapper_functions():
        start_time = time.time()
        function()
        end_time = time.time()
        print(f"{function.__name__} run speed: {end_time - start_time}")
    return wrapper_functions

@speed_calc_decorator
def fast_function():
    for i in range(1000000):
        i * i
    # runtime = time.time()
    # print(runtime - current_time)
        
@speed_calc_decorator
def slow_function():
    for i in range(10000000):
        i * i
    # runtime = time.time()
    # print(runtime - current_time)


# fast_function_output = speed_calc_decorator(fast_function)
# fast_function_output()


# slow_function_output = speed_calc_decorator(slow_function)
# slow_function_output()


fast_function()

slow_function()
