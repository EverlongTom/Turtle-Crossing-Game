from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.all_cars = []
        self.create_car()

    def create_car(self):
        new_car = Turtle()
        new_car.shape("square")
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.penup()
        new_car.color(random.choice(COLORS))
        new_car.goto(300, random.randrange(-250, 270))
        self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            car.backward(MOVE_INCREMENT)
