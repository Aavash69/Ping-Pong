from turtle import Turtle

class ScoreBoard(Turtle):

    def __init__(self,xposition):
        super().__init__()
        self.penup()
        self.color('white')
        self.hideturtle()
        self.goto(x=xposition, y= 240)
        self.score = 0
        self.display()


    def add_score(self):
        self.clear()
        self.score += 1
        self.display()

    def display(self):
        self.write(f"{self.score}",  font=('Verdana', 40 ,"bold"))
