from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self, x_coordinate, y_coordinate):
        super().__init__()
        self.score = 1
        self.color("black")
        self.hideturtle()
        self.penup()
        self.goto(x_coordinate, y_coordinate)
        self.display_score()

    def display_score(self):
        self.write(f"Level: {self.score}", True, align="center", font=("Courier", 16, "bold"))

    def increase_score(self):
        self.clear()
        self.score += 1
        self.display_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", True, align="center", font=("Courier", 16, "bold"))
