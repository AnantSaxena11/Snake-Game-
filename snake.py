from turtle import Turtle
starting_poritions = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake():
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        
    def create_snake(self):
        for positions in starting_poritions:
            self.add_segments(positions)
    def add_segments(self,positions):
            new_segment = Turtle(shape = "square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(positions)
            self.segments.append(new_segment) 
    def extend(self):
        self.add_segments(self.segments[-1].position())
    def move(self):
        for seg_num in range(len(self.segments)-1,0,-1):
            newx = self.segments[seg_num-1].xcor()
            newy = self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(newx,newy)
        self.segments[0].forward(MOVE_DISTANCE)
        
    def up(self):
        if(self.segments[0].heading()!=UP):
            self.segments[0].setheading(90)
        # self.move()
    def left(self):
        if(self.segments[0].heading()!=RIGHT):
            self.segments[0].setheading(180)
        # self.move()
    def down(self):
        if(self.segments[0].heading()!=UP):
            self.segments[0].setheading(270)
        # self.move()
    def right(self):
        if(self.segments[0].heading()!=LEFT):
            self.segments[0].setheading(0)
        # self.move()
        
        