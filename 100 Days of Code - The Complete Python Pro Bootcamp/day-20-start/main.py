from turtle import Screen
from food import Food
from snake import Snake
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("How hungry is Nagini?")
screen.tracer(0)

# Create a snake body
nagini = Snake()
food = Food()

screen.listen()
screen.onkey(nagini.up, "Up")
screen.onkey(nagini.down, "Down")
screen.onkey(nagini.left, "Left")
screen.onkey(nagini.right, "Right")

# Move the snake
game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    nagini.move()

    if nagini.head.distance(food) < 15:
        food.refresh()


# Create snake food

# Detect a collision with food

# Create a scoreboard

# Detect collision with wall

# Detect collision with tail

















screen.exitonclick()