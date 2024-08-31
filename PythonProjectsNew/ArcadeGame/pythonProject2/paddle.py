from turtle import Turtle

paddle_speed = 40

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def up(self):
        if self.ycor() < 230:  # Correct condition to move up
            new_y = self.ycor() + paddle_speed
            self.goto(self.xcor(), new_y)

    def down(self):
        if self.ycor() > -230:  # Correct condition to move down
            new_y = self.ycor() - paddle_speed
            self.goto(self.xcor(), new_y)

    def reset_paddle(self, position):
        self.goto(position)
