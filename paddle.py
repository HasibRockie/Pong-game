from turtle import Turtle

class paddle(Turtle):

    def __init__(self,name,x_pos,y_pos):
        super().__init__()
        self.name = name
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.penup()
        self.setheading(90)
        self.shape('square')
        self.stretchLen = 5
        self.stretchWidth = 1
        self.shapesize(self.stretchWidth,self.stretchLen)
        self.goto(self.x_pos,self.y_pos)
        self.color('white')

    def up(self):
        if self.ycor() < 250:
            self.forward(50)

    def down(self):
        if self.ycor() > -250:
            self.backward(50)
