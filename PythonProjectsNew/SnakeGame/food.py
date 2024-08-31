import random
from turtle import Turtle

class Food(Turtle):
    def __init__(self):  # Fixed constructor method (was __int__)
        super().__init__()  # Fixed the call to the superclass constructor (was __int__)
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)  # Adjusted size to make food smaller
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
