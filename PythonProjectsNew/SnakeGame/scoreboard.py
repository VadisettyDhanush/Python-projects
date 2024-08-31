from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        try:
            with open("../../PythonProjects/SnakeGame/snake_highscore.txt", mode="r") as file:
                high_score_value = file.read().strip()
                self.high_score = int(high_score_value) if high_score_value else 0
        except (FileNotFoundError, ValueError):
            self.high_score = 0

        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=("Arial", 24, "normal"))

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("../../PythonProjects/SnakeGame/snake_highscore.txt", mode="w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()  # Refresh the scoreboard with the reset score and updated high score
