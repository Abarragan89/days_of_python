from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "bold")


with open("data.txt") as file:
    saved_high_score = file.read()


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as file:
            self.high_score = int(file.read())
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
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.display_score()

