from turtle import Turtle
FONT = ("Courier", 15, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-260, 260)
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def update_scoreboard(self):
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}", font=FONT)

    def game_over(self):
        board = Turtle()
        board.hideturtle()
        board.penup()
        board.write("GAME OVER", align="center", font=FONT)

