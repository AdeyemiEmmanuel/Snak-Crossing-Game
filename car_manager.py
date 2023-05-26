from turtle import Turtle
from random import randint, choice
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():

    def __init__(self):
        self.all_cars = []

    def create_car(self):
        chance = randint(1, 6)
        if chance == 1:
            car = Turtle()
            car.shape("square")
            car.penup()
            car.shapesize(1, 2)
            car.setheading(180)
            car.color(choice(COLORS))
            cor_x = 300
            cor_y = randint(-250, 250)
            car.goto(x=cor_x, y=cor_y)
            self.all_cars.append(car)

    def move(self):
        for car in self.all_cars:
            car.forward(STARTING_MOVE_DISTANCE)

    def increase_speed(self):
        global STARTING_MOVE_DISTANCE
        STARTING_MOVE_DISTANCE += MOVE_INCREMENT
