import random
import turtle as t

t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

tim = t.Turtle()
tim.speed("fastest")

current_heading = 0

while current_heading <= 360:
    tim.color(random_color())
    tim.circle(100)
    current_heading += 1
    tim.setheading(current_heading)

screen = t.Screen()
screen.exitonclick()
