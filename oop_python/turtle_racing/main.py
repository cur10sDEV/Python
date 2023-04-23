import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=700, height=600)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

turtles = []
colors = ["purple", "indigo", "green", "yellow", "orange", "red"]

x = -325
y = -125
for i in range(0, 6):
    tim = Turtle(shape="turtle")
    tim.color(colors[i])
    tim.penup()
    tim.goto(x=x, y=y)
    turtles.append(tim)
    y += 50


is_race_on = False

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() >= 315:
            if turtle.color()[0] == user_bet:
                print(f"You win. The {turtle.color()[0]} is the winner.")
            else:
                print(f"You Lose. The {turtle.color()[0]} is the winner.")
            is_race_on = False
            break
        turtle.forward(random.randint(1, 11))

screen.exitonclick()
