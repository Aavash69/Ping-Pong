from turtle import Screen, Turtle
from paddle import Paddle
from border import Border
from ball import Ball
from scoreboard import ScoreBoard

import time


class Display(Turtle):

    def __init__(self, xposition):
        super().__init__()
        self.penup()
        self.color('white')
        self.hideturtle()
        self.goto(x=xposition, y=0)
        if xposition != 0:
            self.write("You win!", font=("Verdana", 16, "bold"))
        else:
            self.write("You draw", font=("Verdana", 16, "bold"))


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title("Pong")
game_is_on = True
screen.tracer(0)

for position in range(300, -350, -50):
    lines = Border(position)

ball = Ball()
pad = Paddle(xposition=380)
padd = Paddle(xposition=-390)
pad_score = ScoreBoard(xposition=150)
padd_score = ScoreBoard(xposition= -150)

delay =0.1
while game_is_on:

    screen.listen()
    screen.update()
    time.sleep(delay)
    if pad.distance(ball) < 50 and ball.xwcor() > 360:
        ball.change_x()
        pad_score.add_score()
        if delay > 0.035:
            delay -= 0.005

    elif padd.distance(ball) < 50 and ball.xcor() < -370:
        ball.change_x()
        padd_score.add_score()
        if delay > 0.035:
            delay -= 0.005


    if ball.xcor() > 380 or ball.xcor() < -390:
        game_is_on = False
        if padd_score.score > pad_score.score:
            dis = Display(xposition=-200)
        elif padd_score.score < pad_score.score:
            dis = Display(xposition=200)
        elif padd_score.score == pad_score.score:
            dis = Display(xposition=0)

    ball.move()
    screen.onkey(pad.up,key="Up")
    screen.onkey(pad.down, key="Down")
    screen.onkey(padd.up,key="w")
    screen.onkey(padd.down,key="s")















screen.exitonclick()