import turtle
from turtle import Turtle, Screen
from paddle import paddle
from ball import Ball
import time
from scoreboard import Scoreboard
from players import players

screen = Screen()
screen.tracer(0)
screen.setup(height=600,width=1000)
screen.bgcolor("black")

x = turtle.textinput("Enter the name","First player:")
y = turtle.textinput("Enter the name","Second player:")

screen.listen()

player_1 = players(x,(-400,240))
player_1 = players(y,(400,240))

l_paddle = paddle(x,-480,0)
r_paddle = paddle(y,480,0)





screen.onkey(r_paddle.up,"Up")
screen.onkey(r_paddle.down,"Down")

screen.onkey(l_paddle.up,"w")
screen.onkey(l_paddle.down,"s")

ball = Ball()
score_l = Scoreboard((-70,220))
score_r = Scoreboard((70,220))
score_l.mid()


game_is_on = True
while game_is_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()

    if ball.ycor() >280 or ball.ycor() <-280:
        ball.bounce()

    if (ball.distance(r_paddle) < 50 and ball.xcor() >460) or (ball.distance(l_paddle) < 50 and ball.xcor() < -460):
        ball.reflect()

    if ball.xcor() > 480:
        score_l.score_update()
        ball.reset()
    elif ball.xcor() < -480:
        score_r.score_update()
        ball.reset()

    if score_l.score ==10 :
        score_l.gameover(l_paddle.name)
        game_is_on = False
    elif score_r.score == 10:
        score_l.gameover(r_paddle.name)
        game_is_on = False






screen.exitonclick()
