
# def foo(a, b=4, c=6):
#     print(a, b, c)

# foo(4, 9)

# def add(*args):
#     result = 0
#     for n in args:
#         result += n
#     return result

# print(add(3, 6, 8))

# # Using **kwargs allows use to specify mulitple keywords and assign values 
# def calculate(n, **kwargs):
#     print(kwargs)
#     # for key,value in kwargs.items():
#     #     print(key)
#     #     print(value)
#     # print(kwargs["add"])
#     n += kwargs["add"]
#     n *= kwargs["multiply"]
#     print(n)


# calculate(2, add=3, multiply=5)

# class Car:
#     def __init__(self, **kw):
#         # self.make = kw["make"]
#         # self.model = kw["model"]
#         self.make = kw.get("make")
#         self.model = kw.get("model")

# my_car = Car(make="Nissan", model="GT-R")
# print(my_car.make)
# print(my_car.model)


# def bar(spam, eggs, toast='yes please!', ham=0):
#     print(spam, eggs, toast, ham)
 
# bar(toast='nah', spam=4, eggs=2)


# def all_aboard(a, *args, **kw): 
#     print(a, args, kw)
 
# all_aboard(4, 7, 3, 0, x=10, y=64)


a = 14
b = 24
c = 44
d = 64
e = -5

print((a * b) + c)
print(a * (b + c))
