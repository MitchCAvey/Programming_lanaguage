from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 268)
        # self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))
        self.hideturtle()
        self.update_scoreboard()
    
    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        # self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))
        self.update_scoreboard()

