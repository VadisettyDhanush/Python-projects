import turtle as t
import time
from food import Food
from snake import Snake
from scoreboard import Scoreboard

screen = t.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)  # Turn off the animation

snake = Snake()
food = Food()
scoreboard=Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    #Detect collision with food
    if snake.head.distance(food)<20:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
    #Detect collision with wall
    if snake.head.xcor() >280 or snake.head.xcor() < -280 or snake.head.ycor()>280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()

    #Detect collision with body
    for segment in snake.segments:
        if segment==snake.head:
            pass
        elif snake.head.distance(segment)<10:
            scoreboard.reset()
            snake.reset()






screen.exitonclick()
