from turtle import Turtle, Screen
import random

t = Turtle()
screen = Screen()
screen.bgcolor("black")
t.color("white")

h = t.pos()
t.speed(500)
t.fd(1)

while t.pos() != h:
    t.lt(random.randint(1,360))
    t.fd(random.randint(1,5))