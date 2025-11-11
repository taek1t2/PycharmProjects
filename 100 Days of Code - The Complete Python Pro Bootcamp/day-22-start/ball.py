from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(1)
        self.penup()


    def move(self):
        new_x = self.xcor() + 10
        new_y = self.ycor() + 10
        self.goto(new_x, new_y)


    def bounce(self):
        top_y = 300
        bottom_y = -300
        if self.ycor() > top_y or self.ycor() < bottom_y:
            self.setheading(-self.heading())

