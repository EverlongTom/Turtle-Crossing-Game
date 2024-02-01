from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)
        self.move_speed = 0.1

    def move(self):
        self.forward(MOVE_DISTANCE)

    def finish_line(self):
        self.goto(STARTING_POSITION)
        self.move_speed *= 0.7
