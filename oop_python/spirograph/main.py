import random
import turtle as t

tim = t.Turtle()
t.colormode(255)
tim.pensize(2)
tim.speed("fastest")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    gen_color = (r, g, b)
    return gen_color


directions = [0, 90, 180, 270]


def draw_spirograph(gap_size):
    for i in range(int(360/gap_size)):
        color = random_color()
        tim.color(color)
        tim.setheading(tim.heading() + gap_size)
        tim.circle(80)


draw_spirograph(5)

screen = t.Screen()
screen.exitonclick()
