from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        self.refresh()
        
    def refresh(self):
        randomm_x = random.randint(-280,280)
        randomm_y = random.randint(-280,280)
        self.goto(randomm_x,randomm_y)
        
        