from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

colors = ["red", "orange", "yellow", "green", "blue", "purple"] # Provides racing turtles a color
y_positions = [-70, -40, -10, 20, 50, 80] # Starting points for racing turtles
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index]) # Places racing turtles at the starting line
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230: # Checks if a turtle has reached the finish line
            is_race_on = False # If so, end the loop
            winning_color = turtle.pencolor() # Record the color of the turtle that won
            if winning_color == user_bet: 
                print(f"You've won! the {winning_color} turtle is the winner!")
            else: 
                print(f"You've lost! the {winning_color} turtle is the winner!")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()