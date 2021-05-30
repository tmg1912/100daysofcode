from turtle import Turtle

ALIGNMENT = 'center'
FONT = ("Courier", 12, 'bold')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score = 0
        with open('/Users/tejas_b6f/Desktop/data.txt') as file:
            self.high_score = int(file.read())
        self.goto(0, 280)
        self.color("white")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('C:/Users/tejas_b6f/Desktop/data.txt',mode='w') as data:
                data.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()
