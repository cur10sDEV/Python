from turtle import Turtle


class Paddle(Turtle):
	def __init__(self, position):
		super().__init__()
		self.color("white")
		self.shape("square")
		self.penup()
		self.setheading(90)
		self.shapesize(stretch_wid=1, stretch_len=5)
		self.goto(position)
		self.speed(0)

	def move_up(self):
		if self.ycor() < 280:
			new_y = self.ycor() + 40
			self.goto(self.xcor(), new_y)

	def move_down(self):
		if self.ycor() > -280:
			new_y = self.ycor() - 40
			self.goto(self.xcor(), new_y)