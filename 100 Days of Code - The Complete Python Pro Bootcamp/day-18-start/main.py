# from turtle import Turtle, Screen

import turtle as t
import random

timmy = t.Turtle()
timmy.shape("turtle")
timmy.fillcolor("Seagreen")
timmy.speed("fastest")
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    pick_color = (r, g, b)
    return pick_color


# Drawing spirograph
def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        timmy.color(random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + size_of_gap)

draw_spirograph(10)


# Random Walk
line_colors = ["navy", "dark green", "teal", "dark red", "orange", "slate blue"]
directions = [0, 90, 180, 270]
timmy.color(random.choice(line_colors))
for to_move in range(300):
    timmy.color(random_color())
    timmy.pensize(10)
    timmy.forward(30)
    timmy.right(random.choice(directions))

# Making shapes continuously in different colors
shape_data = {
    "triangle": {"sides": 3, "colors": "red"},
    "square": {"sides": 4, "colors": "blue"},
    "pentagon": {"sides": 5, "colors": "purple"},
    "hexagon": {"sides": 6, "colors": "sienna4"},
    "heptagon": {"sides": 7, "colors": "springgreen"},
    "octagon": {"sides": 8, "colors": "tomato"},
    "nonagon": {"sides": 9, "colors": "violetred4"},
    "decagon": {"sides": 10, "colors": "turquoise4"}
}

def draw_shapes(sides):
    side_length = 100
    angle = 360 / sides
    for to_move in range(sides):
        timmy.forward(side_length)
        timmy.right(angle)

for value in shape_data.items():
    shape_sides = value["sides"]
    shape_color = timmy.pencolor(value["colors"])
    draw_polygon = draw_shapes(shape_sides, shape_color)
    print(draw_polygon)


# Draw Dashed Line
for _ in range(30):
    timmy.forward(10)
    timmy.penup()
    timmy.forward(5)
    timmy.pendown()

# Draw a square - easier / painful approach
timmy.forward(200)
timmy.right(90)
timmy.forward(200)
timmy.right(90)
timmy.forward(200)
timmy.right(90)
timmy.forward(200)

# Draw a square - My shorter approach
def draw_square():
    timmy.forward(200)
    timmy.right(90)

for to_move in range(4):
    draw_square()


















screen = t.Screen()
screen.exitonclick()