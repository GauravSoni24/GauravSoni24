from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed('fastest')
        self.color('orange')
        self.refresh()

    def refresh(self):
        self.goto(x=random.randint(-280, 285), y=random.randint(-280, 270))