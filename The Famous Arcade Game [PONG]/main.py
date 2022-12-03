# Pong (The Famous Arcade Game) using Python
from turtle import Screen
from paddle import Paddle
from ball import Ball
import time      # To add delay in the movement of the ball
from scoreboard import Scoreboard

screen = Screen()      # Creating a screen object from Screen Class
screen.bgcolor("black")     # setting the background colour of the screen
screen.setup(width=800, height=600)
screen.title("The Famous Arcade Game - PONG")
screen.tracer(0)  # stop the animation

screen.listen()    # listens for the keyboard input

r_paddle = Paddle((350, 0))  # passing values in tuples
l_paddle = Paddle((-350, 0))
ball = Ball()
score = Scoreboard()


screen.listen()      # listens for the keyboard input
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


game_is_on = True  # This is done to create a while loop
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()  # updates the screen and shows the animation which is removed by tracer(0)
    ball.move()     # calling a method from Ball Class

    # Collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detecting collision with the paddles

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_x()
        score.r_point()

    if ball.distance(l_paddle) < 50 and ball.xcor() > -320:
        ball.bounce_x()
        score.l_point()

    # Dectect R Paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()

    # Dectect L Paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()

screen.exitonclick()
