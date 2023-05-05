from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

paddle=Turtle()
screen= Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("PONG GAME")
screen.tracer(0)

r_paddle= Paddle((370, 0))
l_paddle= Paddle((-370, 0))
ball=Ball()
score=Scoreboard()

screen.listen()
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")

screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")


game_is_on= True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detect collision with wall
    if ball.ycor() >280 or ball.ycor() <-280:
        ball.bounce_y()

    #     detect collision with paddle
    if ball.distance(r_paddle)<50 and ball.xcor()> 320 or ball.distance(l_paddle)<50 and ball.xcor()<-320:
        ball.bounce_x()

    #     Detect R paddle misses
    if ball.xcor()>380:
        ball.reset_position()
        score.l_point()

    #     Detect L paddle misses
    if ball.xcor()<-380:
        ball.reset_position()
        score.r_point()

screen.exitonclick()