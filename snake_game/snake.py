from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
extra_pieces = [(-60, 0), (-80, 0), (-100, 0), (-120, 0), (-140, 0), (160, 0)]
# STARTING_POSITIONS.extend(extra_pieces)


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.speed = 20
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def move_snake(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(self.speed)

    def up(self):
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)

    def down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)

    def right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)

    def left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)

    def add_segment(self, position):
        snake_square = Turtle("square")
        snake_square.penup()
        snake_square.color("white")
        snake_square.goto(position)
        self.segments.append(snake_square)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def extends(self):
        print("the position added", self.segments[-1].position())
        self.add_segment(self.segments[-1].position())






