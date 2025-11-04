# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 45)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.r
#     b = color.rgb.r
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

import turtle as t
import random

tae = t.Turtle()
tae.shape("turtle")



color_list = [(232, 232, 232), (1, 1, 1), (229, 229, 229), (239, 239, 239), (122, 122, 122), (71, 71, 71), (238, 238, 238), (220, 220, 220), (226, 226, 226), (93, 93, 93), (178, 178, 178), (151, 151, 151), (35, 35, 35), (7, 7, 7), (205, 205, 205), (221, 221, 221), (168, 168, 168), (1, 1, 1), (3, 3, 3), (4, 4, 4), (80, 80, 80), (132, 132, 132), (81, 81, 81), (116, 116, 116), (11, 11, 11), (117, 117, 117), (131, 131, 131), (230, 230, 230), (243, 243, 243), (70, 70, 70), (186, 186, 186), (91, 91, 91), (128, 128, 128)]

# 10 x 10 random dots
# 20 in size of the circle
# 50 paces apart

screen = t.Screen()
screen.exitonclick()