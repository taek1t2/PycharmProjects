import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(player.go_up, "Up")


collision_distance = 25
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.moving_cars()

    for every_car in car.all_cars:
        if player.distance(every_car) < collision_distance:
            score.game_over()
            game_is_on = False

    if player.at_finish_line():
        player.start_over()
        car.level_up()
        score.level_up()

    screen.update()
screen.exitonclick()