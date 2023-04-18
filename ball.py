from turtle import Turtle
ANGLE = 50


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.setheading(ANGLE)
        self.ball_speed = 0.25

    def move(self):
        self.penup()
        self.forward(self.ball_speed)

    def normal_speed(self):
        self.ball_speed = 0.15

    def faster(self):
        self.ball_speed += 0.005

    def bounce(self):
        if self.heading() <= 360:
            self.setheading(self.heading() + 90)
        else:
            self.setheading((self.heading() - 360) + 90)

    def r_reset(self):
        self.goto(0, 0)
        self.right(90)

    def l_reset(self):
        self.goto(0, 0)
        self.right(90)
