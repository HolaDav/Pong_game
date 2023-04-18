from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("My pong game")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

ball = Ball()

score = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    ball.move()
    if ball.ycor() > 296 or ball.ycor() < -296:
        ball.bounce()
    if ball.xcor() > 340 and ball.distance(r_paddle) < 50 or ball.xcor() < -340 and ball.distance(l_paddle) < 50:
        ball.faster()
        ball.bounce()

    if ball.xcor() > 380:
        ball.l_reset()
        score.l_point()
        ball.normal_speed()
    elif ball.xcor() < -380:
        ball.r_reset()
        score.r_point()
        ball.normal_speed()

screen.exitonclick()
