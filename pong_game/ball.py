from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.width(10)
        self.penup()
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_len=0.7, stretch_wid=0.7)
        self.setheading(200)
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move_ball(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_move *= -1
        self.move_speed *= 0.9

    def paddle_bounce(self):
        self.x_move *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.paddle_bounce()





