import turtle
import colorsys
import math
import random

random.seed(7)
TILT = 0.45

screen = turtle.Screen()
screen.setup(780, 480)
screen.bgcolor("#03030b")
screen.tracer(30)

t = turtle.Turtle()
t.hideturtle()
t.speed(0)
