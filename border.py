from turtle import Turtle


class Border(Turtle):
    def __init__(self,yposition):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.penup()
        self.shapesize(stretch_wid=1.5,stretch_len=0.25)
        self.goto(x=0,y=yposition)