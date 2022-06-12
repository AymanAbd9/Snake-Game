from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake():
    def __init__(self):
        self.squares = []
        self.create_snake()
        self.head = self.squares[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_square = Turtle(shape="square")
            new_square.color("white")
            new_square.penup()
            new_square.setposition(position)
            self.squares.append(new_square)

    def move(self):
        # Move body of the snake
        for last_square in range(len(self.squares) - 1, 0, -1):
            x = self.squares[last_square - 1].xcor()
            y = self.squares[last_square - 1].ycor()
            self.squares[last_square].setposition(x, y)

        # Move head of the snake
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if(self.head.heading() != DOWN):
            self.head.setheading(UP)

    def down(self):
        if(self.head.heading() != UP):
            self.head.setheading(DOWN)

    def left(self):
        if(self.head.heading() != RIGHT):
            self.head.setheading(LEFT)

    def right(self):
        if(self.head.heading() != LEFT):
            self.head.setheading(RIGHT)