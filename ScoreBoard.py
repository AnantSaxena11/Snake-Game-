from turtle import Turtle
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.Score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,270)
        self.write(f"Score :{self.Score}",align="center",font =("Arial",24,"normal"))
    def refresh(self):
        self.Score += 1
        self.clear()
        self.write(f"Score :{self.Score}",align="center",font =("Arial",24,"normal"))
    def gameover(self):
        self.clear()
        self.write(f"Game over Final Score :{self.Score}",align="center",font =("Arial",24,"normal"))
        