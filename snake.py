from turtle import Turtle

#Constant creation
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    #Constructor
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]


    # Sanke creation method
    #Created 3 square blocks
    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)


    def add_segment(self,position):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)


    #extend snake
    def extend(self):
        self.add_segment(self.segments[-1].position())


    # Snake movement in forward direction
    def move(self):
            # Dsscription--> last turtle moved to second position
            # and second moved to first one position
            # and first one forwards 20
            for seg_num in range(len(self.segments) - 1, 0, -1):
                # print(seg_num)
                new_x = self.segments[seg_num - 1].xcor()
                new_y = self.segments[seg_num - 1].ycor()
                # print((new_x,new_y))
                self.segments[seg_num].goto(new_x, new_y)
            self.segments[0].forward(MOVE_DISTANCE)

# Snake movement
    # left movement
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    'right movement'
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    #Moving Up
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    #moving down
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)


