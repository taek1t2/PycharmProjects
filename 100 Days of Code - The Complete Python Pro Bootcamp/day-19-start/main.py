from turtle import Turtle, Screen

tae = Turtle()
screen = Screen()

def move_forwards():
    tae.forward(10)

def move_backwards():
    tae.backward(10)

def move_right():
    new_heading = tae.heading() - 10
    tae.setheading(new_heading)

def move_left():
    new_heading = tae.heading() + 10
    tae.setheading(new_heading)

def clear_out():
    tae.clear()

screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="d", fun=move_right)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="c", fun=clear_out)


screen.exitonclick()