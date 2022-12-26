from turtle import Turtle, Screen
from pong import Pong
from pong_ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

left_pong = Pong("left")
right_pong = Pong("right")
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(key="w", fun=left_pong.up)
screen.onkeypress(key="s", fun=left_pong.down)
screen.onkeypress(key="Up", fun=right_pong.up)
screen.onkeypress(key="Down", fun=right_pong.down)




game_is_on = True

while game_is_on:
    # Detect collision with the upper and lower wall
    if ball.ycor() < -280 or ball.ycor() > 280:
        ball.bounce()

    if (abs(ball.ycor()-left_pong.ycor())<50 and ball.xcor()<-360):
        ball.reverse()

    if (abs(ball.ycor()-right_pong.ycor())<50 and ball.xcor()>360):
        ball.reverse()

    if (abs(ball.ycor()-right_pong.ycor())>=50 and ball.xcor()>360):
        scoreboard.l_score += 1
        scoreboard.update_scoreboard()
        ball.reset()

    if (abs(ball.ycor()-left_pong.ycor())>=50 and ball.xcor()<-360):
        scoreboard.r_score += 1
        scoreboard.update_scoreboard()
        ball.reset()

    screen.update()
    time.sleep(0.05)
    ball.move()


















screen.exitonclick()