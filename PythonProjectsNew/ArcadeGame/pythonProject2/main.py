from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Set up the screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

# Create paddles and ball
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

# Listen for keyboard input
screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

# Main game loop
game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # Wall collision
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()

    # Paddle collision
    if (ball.xcor() > 320 and ball.distance(r_paddle) < 50) or (ball.xcor() < -320 and ball.distance(l_paddle) < 50):
        ball.bounce_x()

    # Left paddle miss
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()
        r_paddle.reset_paddle((350, 0))
        l_paddle.reset_paddle((-350, 0))

    # Right paddle miss
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
        l_paddle.reset_paddle((-350, 0))
        r_paddle.reset_paddle((350, 0))

screen.exitonclick()
