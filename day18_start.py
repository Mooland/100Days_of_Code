# from turtle import Screen, Turtle

import turtle as t
import random


tim = t.Turtle()
t.colormode(255)

def random_rgb():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return(r,g,b)
turn_base = [90,180,270,0]
tim.shape("circle")
tim.pensize(2)
tim.speed(0)

def random_walk(steps):
    for step in range(steps):
        tim.color(random_rgb())
        tim.setheading(random.choice(turn_base))
        tim.forward(30)


def spirograph(number_of_circles):
    for circle in range(number_of_circles):
        tim.color(random_rgb())
        tim.circle(100)
        tim.left(360/number_of_circles)


screen = t.Screen()
screen.exitonclick()