from turtle import Screen
from scoreboard import Scoreboard
from crossing_turtle import CrossingTurtle
from car import CarManager
import time

# Set up screen
screen = Screen()
screen.setup(width=800, height=500)
screen.tracer(0)


# Instantiate Classes
crossing_turtle = CrossingTurtle()
scoreboard = Scoreboard(-350, 215)


# Make Car Manager instance
car_manager = CarManager()

# Set up Key Binds
screen.listen()
screen.onkey(crossing_turtle.move_forward, "Up")


# Game Loop
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_car()
    for car in car_manager.all_cars:
        if crossing_turtle.distance(car) < 15:
            game_is_on = False
    if crossing_turtle.ycor() > 230:
        scoreboard.increase_score()
        car_manager.level_up()
        crossing_turtle.goto(0, -220)

scoreboard.game_over()




screen.exitonclick()









