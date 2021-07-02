from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.goto(0,0)
        self.penup()
        self.speed('slow')
        self.xmove = 10
        self.ymove = 10
        self.ball_speed = 0.1


    def move(self):
        self.new_xcor = self.xcor() + self.xmove
        self.new_ycor = self.ycor() + self.ymove
        self.goto(self.new_xcor, self.new_ycor)
    def bounce(self):
        self.ymove *= -1
        self.move()

    def reflect(self):
        self.xmove *= -1
        self.ball_speed *= 0.75
        self.move()

    def reset(self):
        self.goto(0,0)
        self.reflect()
        self.ball_speed = 0.1








# and self.new_ycor < 230 and self.new_xcor > -470 and self.new_ycor > -230