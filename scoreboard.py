from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Arial', 24, 'normal')


class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.current_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(x=0, y=260)
        self.write(f"SCORE: {self.current_score}",  align=ALIGNMENT,
                   font=FONT)

    def add_point(self):
        self.clear()
        self.current_score += 1
        self.write(f"SCORE: {self.current_score}",  align=ALIGNMENT,
                   font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER!",  align=ALIGNMENT,
                   font=FONT)
