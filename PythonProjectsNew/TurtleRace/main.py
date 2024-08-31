logo ="""
#  _______           _   _
# |__   __|         | | | |
#    | | ___   ___ | |_| |_ ___
#    | |/ _ \ / _ \| __| __/ _ \
#    | | (_) | (_) | |_| ||  __/
#    |_|\___/ \___/ \__|\__\___|
"""


print(logo)

import random
import turtle as t

screen=t.Screen()
screen.setup(width=500,height=400)
user_bet=screen.textinput(title="Make your bet",prompt="which turtle will win the race? Enter a color: " )

t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)
rainbow_colors = ['red', 'orange', 'yellow', 'green', 'blue']
all_turtle=[]

race_on=False
for i in range(5):
    timA = t.Turtle(shape="turtle")
    timA.color(rainbow_colors[i])
    timA.penup()
    timA.goto(x=-230, y=-100+i*50)
    all_turtle.append(timA)

race_on = True
while race_on:

    for turtle in all_turtle:
        rand_dist = random.randint(0, 10)
        turtle.forward(rand_dist)
        if turtle.xcor()>230:
            race_on = False
            winning_color=turtle.pencolor()

            if winning_color==user_bet:
                print("You Won")
            else:
                print("You Lose")



screen.exitonclick()



