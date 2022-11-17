from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self, x_coordinate, y_coordinate):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x_coordinate, y_coordinate)
        self.display_score()

    def display_score(self):
        self.write(self.score, True, align="center", font=("Courier", 30, "bold"))

    def increase_score(self):
        self.clear()
        self.score += 1
        self.display_score()
