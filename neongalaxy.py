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
t.penup()

def glow(h, v=1.0):
return colorsys.hsv_to_rgb(h % 1, 0.7,v)

def place(x, y)
y *= 0.55
c, s = math.cos(TILT), math.sin(TILT)
t.goto(x * c - y * s, x * s + y * c)

def stars():
  for _ in range(140)
  x = random.randint
