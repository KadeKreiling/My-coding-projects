from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Score_Board

screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Pong")
screen.tracer(0)
player1 = Paddle()
player2 = Paddle()
player1.player_1_position()
player2.player_2_position()
ball = Ball()
score_board = Score_Board()

screen.listen()
screen.onkey(player2.move_up, "Up")
screen.onkey(player2.move_down, "Down")
screen.onkey(player1.move_up, "w")
screen.onkey(player1.move_down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    ball.ball_move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    if ball.xcor() > 350 and ball.distance(player2) < 50:
        ball.paddle_bounce()
        ball.speed_up()

    if ball.xcor() < -350 and ball.distance(player1) < 50:
        ball.paddle_bounce()
        ball.speed_up()

    if ball.xcor() > 400:
        ball.reset_position()
        player1.player_1_position()
        player2.player_2_position()
        score_board.p1_point()

    if ball.xcor() < -400:
        ball.reset_position()
        player1.player_1_position()
        player2.player_2_position()
        score_board.p2_point()


screen.exitonclick()

