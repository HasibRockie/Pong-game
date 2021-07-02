from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self,position):
        super().__init__()
        self.score = 0
        self.position = position
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(self.position)
        self.write(self.score, align="center",font=("Arial",60,"bold"))

    def mid(self):
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0,220)
        self.write(f"-", align="center", font=("Arial", 60, "bold"))

    def score_update(self):
        self.score +=1
        self.clear()
        self.goto(self.position)
        self.write(f"{self.score}", align="center",font=("Arial",60,"bold"))
        self.mid()

    def gameover(self,player):
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0,0)
        self.write(f"{player} is the winner", align="center", font=("Arial", 40, "bold"))


