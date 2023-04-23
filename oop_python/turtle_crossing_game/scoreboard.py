from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto(x=-240, y=260)
        self.write(f'Level: {self.level}', align=ALIGNMENT, font=FONT)

    def increment(self):
        self.clear()
        self.level += 1
        self.write(f'Level: {self.level}', align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over", align=ALIGNMENT, font=FONT)
