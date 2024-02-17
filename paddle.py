from turtle import Turtle

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len= 5)
        self.color("white")
        self.penup()
        self.left(90)
        self.speed("fastest")


    def player_1_position(self):
        self.setpos(-380, 0)

    def player_2_position(self):
        self.setpos(370, 0)


    def move_up(self):
        self.forward(20)

    def move_down(self):
        self.backward(20)

