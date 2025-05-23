import csv
import pandas
import turtle


screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blankstatesimg.gif"

screen.addshape(image)

turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", 
                                    prompt="What's another State's name?").title()
    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        # for state in all_states:
        #     if state not in guessed_states:
        #         missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    # If answer_state is one of the states in all the states of the 50_states.csv
    if answer_state in all_states:
        # If they got it right:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        # Create a turle to write the name of the state at the state's x and y coordate
        # t.write(answer_state)
        t.write(state_data.state.item())

# states_to_learn.csv


# How to find the x and y coordinate from clicking on any given location
# def get_mouse_click_coor(x, y):
#     print(x, y)

# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

# screen.exitonclick()

