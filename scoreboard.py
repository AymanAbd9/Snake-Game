from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 12, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.setposition(0, 270)
        self.current_score = 0
        self.refresh_score()
        

    def refresh_score(self):
        self.clear()
        self.write(f"Score: {self.current_score}", move=False, font=FONT, align=ALIGNMENT)

    def increase_score(self):
        self.current_score += 1
        self.refresh_score()