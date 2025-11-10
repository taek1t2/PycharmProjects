from encodings.punycode import selective_find
from turtle import Turtle

class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        paddle.color("white")
        paddle.shapesize(stretch_wid=5, stretch_len=1)
        paddle.penup()
        paddle.setpos(350, 0)



    def go_up():
        new_y = paddle.ycor() + 20
        paddle.goto(paddle.xcor(), new_y)

    def go_down():
        new_y = paddle.ycor() - 20
        paddle.goto(paddle.xcor(), new_y)
