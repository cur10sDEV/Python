from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        if self.xcor() < 380 or self.ycor() < 280 or self.xcor() > -380 or self.ycor() > -280:
            new_x = self.xcor() + self.x_move
            new_y = self.ycor() + self.y_move
            self.goto(x=new_x, y=new_y)

    def y_bounce(self):
        self.y_move *= -1

    def x_bounce(self):
        self.x_move *= -1

    def reset_position(self):
        self.goto(x=0, y=0)
        self.x_bounce()
        self.move_speed = 0.1
