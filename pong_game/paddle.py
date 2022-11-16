from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x_coordinate, y_coordinate):
        super().__init__()
        self.width(15)
        self.penup()
        self.goto(x_coordinate, y_coordinate)
        self.shape("square")
        self.shapesize(stretch_len=1, stretch_wid=3)
        self.color("white")

    def up(self):
        self.sety(self.ycor() + 10)

    def down(self):
        self.sety(self.ycor() - 10)






