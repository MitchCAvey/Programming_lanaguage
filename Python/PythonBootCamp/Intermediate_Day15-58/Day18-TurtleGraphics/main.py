# from turtle import Screen
# import turtle as t
# import random

# timmy_the_turtle = Turtle()
# timmy_the_turtle.shape("turtle")
#timmy_the_turtle.color("SpringGreen4")
# timmy_the_turtle.color("OrangeRed4")

# for _ in range(4):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(90)


# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)

# for _ in range(15):
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.penup()
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.pendown()

# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray"]
# directions = [0, 90, 180, 270]
# def draw_shape(num_sides):
#     angle = 360 /num_sides
#     for _ in range(num_sides):
#         timmy_the_turtle.forward(100)
#         timmy_the_turtle.right(angle)

# for shape_side_n in range(3, 11):
#     timmy_the_turtle.color(random.choice(colours))
#     draw_shape(shape_side_n)
# tim = t.Turtle()

# t.colormode(255)
# tim.pensize(15)
# tim.speed("fastest")

# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     random_colour = (r, g, b)
#     return random_colour

# for _ in range(200):
#     # tim.color(random.choice(colours))
#     tim.color(random_color())
#     tim.forward(30)
#     tim.setheading(random.choice(directions))

import turtle as t
import random

tim = t.Turtle()
# tim.speed("fastest")
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colour = (r, g, b)
    return colour

tim.speed("fastest")

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

draw_spirograph(6)

screen = t.Screen()
screen.exitonclick()

