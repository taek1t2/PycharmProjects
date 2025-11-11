from turtle import Turtle
from paddle import Paddle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(1)
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = .1


    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)


    def bounce_y(self):
        top_y = 280
        bottom_y = -280
        if self.ycor() > top_y or self.ycor() < bottom_y:
            self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 1

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = .1
        self.bounce_x()