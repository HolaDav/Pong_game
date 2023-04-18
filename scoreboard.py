from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.point()

    def point(self):
        self.write(arg=f"Right Score: {self.r_score}    Left Score: {self.l_score}", align="center",
                   font=("Courier", 25, "normal"))

    def r_point(self):
        self.clear()
        self.r_score += 1
        self.point()

    def l_point(self):
        self.clear()
        self.l_score += 1
        self.point()
