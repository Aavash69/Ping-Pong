from turtle import Turtle


POSITION = 10


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color('purple')
        self.shape('circle')
        self.shapesize(stretch_wid=0.5,stretch_len=0.5)
        self.penup()
        self.addy = 10
        self.addx = 10
        self.speedtest = 1.0

    def change_x(self):
        self.addx *= -1

        while self.speedtest <= 10:
            self.speedtest += 1.0






    def move(self):
        self.speed(self.speedtest)
        if self.ycor() == 280:
            self.addy = - 10

        elif self.ycor() == -280:
            self.addy = 10

        new_x = self.xcor() + self.addx
        new_y = self.ycor() + self.addy

        self.goto(new_x,new_y)


