from turtle import Screen
import time
from player import Player
from scoreboard import Scoreboard
from car_manager import CarManager

screen = Screen()
score = Scoreboard()
player = Player()
car_manager = CarManager()
screen.setup(width=600, height=600)
screen.title("Turtle Crossy Road")
screen.tracer(0)

screen.listen()

screen.onkey(key="Up", fun=player.move_up)

is_game_on = True
while is_game_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_forward()

    if player.ycor() > 260:
        score.increment()
        car_manager.level_up()
        player.reset()

    # Detect collision with cars
    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            score.game_over()
            is_game_on = False


screen.exitonclick()
