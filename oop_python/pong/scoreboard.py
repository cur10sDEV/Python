from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 40, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = {"left": 0, "right": 0}
        self.color("white")
        self.penup()
        self.goto(x=0, y=240)
        self.write(f'{self.score["left"]}\t{self.score["right"]}', align=ALIGNMENT, font=FONT)
        self.hideturtle()

    def increment(self, direction):
        self.clear()
        if direction == "left":
            self.score["right"] += 1
        elif direction == "right":
            self.score["left"] += 1
        self.write(f'{self.score["left"]}\t{self.score["right"]}', align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over", align=ALIGNMENT, font=FONT)
