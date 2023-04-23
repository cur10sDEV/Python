# change folder name to pong only

from turtle import Turtle, Screen
from ball import Ball
from scoreboard import Scoreboard
from paddle import Paddle
import time

screen = Screen()
score = Scoreboard()
ball = Ball()
l_paddle = Paddle((-370, 0))
r_paddle = Paddle((365, 0))
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

x = 0
y = 280
for i in range(8):
	center = Turtle(shape="square")
	center.color("white")
	center.shapesize(stretch_wid=2, stretch_len=0.25)
	center.penup()
	center.goto(x=x, y=y)
	y -= 80

screen.listen()

screen.onkey(key="Up", fun=r_paddle.move_up)
screen.onkey(key="Down", fun=r_paddle.move_down)
screen.onkey(key="w", fun=l_paddle.move_up)
screen.onkey(key="s", fun=l_paddle.move_down)

ball.goto(x=-350, y=200)
is_game_on = True
while is_game_on:
	time.sleep(ball.move_speed)
	# Detect collision with top and bottom wall
	if ball.ycor() > 280 or ball.ycor() < -280:
		ball.y_bounce()

	# Detect collision with paddle
	if (ball.distance(r_paddle) < 50 and ball.xcor() > 340) or (ball.distance(l_paddle) < 50 and ball.xcor() < -340):
		ball.x_bounce()
		ball.move_speed *= 0.9

	# if paddle misses the ball
	if ball.xcor() > 360 or ball.xcor() < - 360:
		if ball.xcor() > 0:
			score.increment(direction="right")
		elif ball.xcor() < 0:
			score.increment(direction="left")
		ball.reset_position()

	if score.score["left"] >= 10 or score.score["right"] >= 10:
		score.game_over()
		is_game_on = False

	ball.move()
	screen.update()

screen.exitonclick()
