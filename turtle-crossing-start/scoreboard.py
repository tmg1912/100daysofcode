from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.level = 1
        self.write(f"Level {self.level}",align='center', font=FONT)

    def update(self):
        self.clear()
        self.level += 1
        self.write(f"Level {self.level}",align='center', font=FONT)

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write("GAME OVER", align='center', font=FONT)
