from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DIST = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
# capital letter variables are to denote constant value


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for positions in STARTING_POSITIONS:
            tuts = Turtle(shape="square")
            tuts.penup()
            tuts.color("white")
            tuts.goto(positions)
            self.segments.append(tuts)  # appending turtles in list

    def move(self):
        for seg_number in range(len(self.segments)-1, 0, -1):
            # making the nxt turtle to come to predecessor place in x axis
            new_x = self.segments[seg_number - 1].xcor()
            # making the nxt turtle to come to predecessor place in y axis
            new_y = self.segments[seg_number - 1].ycor()
            self.segments[seg_number].goto(new_x, new_y)
        self.segments[0].fd(MOVE_DIST)

    def up(self):
        if self.head.heading() != DOWN:
            # self.segments[0].setheading(90) #to reduce repetitve, self.segments[0] is set as self.head
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
