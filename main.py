import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(player.move_speed)
    screen.update()
    random_number = random.randint(1, 100)
    if random_number <= 15:
        car_manager.create_car()

    car_manager.move()

    if player.ycor() > 280:
        player.finish_line()
        scoreboard.new_level()

    for car in car_manager.all_cars:
        if player.distance(car) < 20 and (car.ycor() > player.ycor() or car.ycor() < player.ycor()):
            scoreboard.game_over()
            game_is_on = False

screen.exitonclick()
