from turtle import Turtle

class players(Turtle):

    def __init__(self,player,position):
        super().__init__()
        self.name = player
        self.penup()
        self.color("red")
        self.hideturtle()
        self.position = position
        self.tilt(90)
        self.goto(self.position)
        self.write(self.name,align='center',font=('Courier',30,'normal'))

