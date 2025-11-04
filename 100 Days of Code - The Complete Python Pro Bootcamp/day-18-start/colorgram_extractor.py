# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 45)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

import turtle as t
import random

tae = t.Turtle()
tae.shape("turtle")
tae.speed("fastest")
t.colormode(255)
tae.penup()
tae.goto(-200,-100)

color_list = [(249, 248, 248), (232, 241, 239), (1, 10, 30), (229, 235, 242), (239, 232, 238), (122, 95, 41), (71, 31, 21), (238, 212, 72), (220, 81, 59), (226, 117, 100), (93, 1, 21), (178, 140, 171), (151, 92, 115), (35, 90, 26), (7, 154, 72), (205, 63, 91), (221, 178, 218), (168, 129, 77), (1, 64, 147), (3, 79, 29), (4, 220, 218), (80, 135, 179), (132, 158, 177), (81, 110, 136), (116, 187, 164), (11, 215, 222), (117, 19, 37), (131, 224, 209), (230, 173, 165), (243, 205, 7), (70, 72, 44), (186, 190, 199), (91, 48, 43), (128, 223, 230)]
dot_size = 20
rows = 10
cols = 10
gap = 50

def draw_row(num_dots):
    for dot in range(num_dots):
        tae.dot(dot_size, random.choice(color_list))
        tae.penup()
        tae.fd(gap)

def another_row(num_cols):
    tae.setheading(90)
    tae.forward(gap)
    tae.setheading(180)
    tae.forward(gap * num_cols)
    tae.setheading(0)

for _ in range(rows):
    draw_row(cols)
    if _ < rows - 1:
        another_row(cols)


screen = t.Screen()
screen.exitonclick()

