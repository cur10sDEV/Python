import random
import turtle as t
import colorgram

extracted_colors = colorgram.extract("image.jpg",100)
colors = []

for color in extracted_colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    gen_color = (r, g, b)
    colors.append(gen_color)

tim = t.Turtle()
t.colormode(255)
tim.pensize(22)
tim.speed("fast")
tim.hideturtle()

vertical = 10
tim.penup()
tim.setpos(-225.0, -225.0)

while vertical > 0:
    for i in range(10):
        tim.pencolor(random.choice(colors))
        tim.pendown()
        tim.forward(0)
        tim.penup()
        tim.forward(50)
    current_position = tim.pos()
    tim.setpos(-225.0, current_position[1]+50)
    vertical -= 1

screen = t.Screen()
screen.exitonclick()
