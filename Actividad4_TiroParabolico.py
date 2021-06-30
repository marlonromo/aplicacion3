from random import randrange
from turtle import *

from freegames import vector

ball = vector(-200, -200)
speed = vector(0, 0)
targets = []


def tap(x, y):
 


def inside(xy):
"Return True if xy within screen."
return -200 < xy.x < 200 and -200 < xy.y < 200



def draw():
  
def move():



setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()