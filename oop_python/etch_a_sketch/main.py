from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
screen.listen()


class Move:
    def __init__(self):
        self.key = "space"

    def move_forward(self):
        tim.forward(10)

    def move_backward(self):
        tim.backward(10)

    def move_left(self):
        tim.left(10)

    def move_right(self):
        tim.right(10)

    def clr_scr(self):
        tim.penup()
        tim.home()
        tim.setheading(0)
        tim.clear()
        tim.pendown()


move = Move()
screen.onkey(key="w", fun=move.move_forward)
screen.onkey(key="s", fun=move.move_backward)
screen.onkey(key="a", fun=move.move_left)
screen.onkey(key="d", fun=move.move_right)
screen.onkey(key="c", fun=move.clr_scr)

screen.exitonclick()
