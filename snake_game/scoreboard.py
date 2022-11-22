from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 270)
        self.display_score()

    def display_score(self):
        self.clear()
        text = f"Score: {self.score} High Score: {self.high_score}"
        self.write(text, False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.display_score()

    def reset_scoreboard(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.display_score()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("Game over", False, align=ALIGNMENT, font=FONT)
