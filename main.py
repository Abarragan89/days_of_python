import turtle
from turtle import Turtle, Screen
import random


is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "aqua", "green", "blue", "purple"]
all_turtles = []

start_y_coord = -100

for num in range(0, 6):
    y_coordinate = start_y_coord + (num * 40)
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[num])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_coordinate)
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() >= 230:
            winning_turtle = turtle
            is_race_on = False
            if user_bet == winning_turtle.pencolor():
                print(f"You win! The winner was {winning_turtle.pencolor()}")
            else:
                print(f"You lose! The winner was {winning_turtle.pencolor()}")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)



screen.exitonclick()
