from turtle import Turtle
import time

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.x_move = 10
        self.y_move = 10
        self.ball_speed = .075

    def ball_move(self):
        time.sleep(self.ball_speed)
        self.penup()
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_move *= -1

    def paddle_bounce(self):
        self.x_move *= -1

    def reset_position(self):
        self.goto(0,0)
        self.ball_speed = .075


    def speed_up(self):
        self.ball_speed -= .005



