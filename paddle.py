from turtle import Turtle


class Paddle(Turtle):
    def __init__(self,xposition):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.penup()
        self.setheading(90)
        self.shapesize(stretch_len=5,stretch_wid=0.5)
        self.speed('fastest')
        self.goto(xposition,y=0)


    def up(self):
        self.forward(20)

    def down(self):
        self.back(20)