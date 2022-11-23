from turtle import Turtle


class StateName(Turtle):
    def __init__(self, text, xpos, ypos):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.text = text
        self.goto(xpos, ypos)
        self.display_text()

    def display_text(self):
        self.write(self.text, font=("Arial", 12, "normal"), align="left")

