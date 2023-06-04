from turtle import Turtle
MOVE_DISTANCE = 20
class Snake:
    def __init__(self):
        self.segments = []
        self.x, self.y = 0, 0
        for _ in range(3):
            tim = Turtle(shape='square')
            tim.color('white')
            tim.penup()
            tim.goto(x=self.x, y=self.y)
            self.x += -20
            self.segments.append(tim)

    def add_segment(self):
        new_segment = Turtle()
        new_segment.shape('square')
        new_segment.penup()
        new_segment.goto(self.segments[-1].position())
        self.segments.append(new_segment)
        new_segment.color('white')

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            self.segments[seg_num].goto(self.segments[seg_num - 1].xcor(), self.segments[seg_num - 1].ycor())
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)

    def down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)

    def right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)

    def left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)

    def stop(self):
        self.segments[0].forward(0)