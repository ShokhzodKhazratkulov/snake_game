from turtle import Turtle
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
# the varibles above are called constant varibles which are given final value and cannot be changed
class Snake:

    def __init__(self):
        self.segments = []
        self.snake()
        self.head = self.segments[0]


#TODO: Secondly, we need to create the segments for our snake body with for loop and set position its segments

    def snake(self):

        for create_snake in STARTING_POSITION:
            self.add_segments(create_snake)



    def add_segments(self, create_snake):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(create_snake)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segments(self.segments[-1].position())


#this might be pretty complex but it is for movement of snake body. it is responsible for the there is no intervals
# between segments
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_xcor = self.segments[seg_num - 1].xcor()
            new_ycor = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_xcor, new_ycor)

        self.segments[0].forward(20)
# the lines of code below are methods for managing direction of snake and there is also one condition for don't turn backwards
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def dawn(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
