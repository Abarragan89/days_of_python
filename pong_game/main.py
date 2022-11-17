from turtle import Turtle, Screen
from scoreboard import Scoreboard
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.setup(width=800, height=500)
screen.bgcolor("black")
screen.tracer(0)

# Draw center net
net = Turtle()
net.penup()
net.speed("fastest")
net.width(5)
net.hideturtle()
net.color("white")
net.goto(0, 250)
net.setheading(270)
while net.ycor() > -250:
    net.pendown()
    net.forward(20)
    net.penup()
    net.forward(10)


# Instantiate classes
player_1_score = Scoreboard(-70, 200)
player_2_score = Scoreboard(70, 200)

player_1_paddle = Paddle(-370, 0)
player_2_paddle = Paddle(370, 0)

ball = Ball()


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    # Set up Event Listeners
    screen.listen()
    screen.onkey(player_1_paddle.up, "w")
    screen.onkey(player_1_paddle.down, "s")
    screen.onkey(player_2_paddle.up, "Up")
    screen.onkey(player_2_paddle.down, "Down")

    # Move ball
    ball.move_ball()

    # Detect wall collision
    if ball.ycor() > 240 or ball.ycor() < -240:
        ball.bounce()

    # Detect collision with paddle
    if ball.distance(player_2_paddle) < 50 and ball.xcor() > 340 or \
            ball.distance(player_1_paddle) < 50 and ball.xcor() < -340:
        ball.x_move += 1
        ball.y_move += 1
        ball.paddle_bounce()


    # Check if player has scored
    if ball.xcor() > 370:
        ball.reset_position()
        player_1_score.increase_score()

    if ball.xcor() < -370:
        ball.reset_position()
        player_2_score.increase_score()


screen.exitonclick()
