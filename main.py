from turtle import *
import random
t=Turtle()
colors = ['red', 'green', 'blue', 'yellow', 'orange']
def draw_shape(no_of_sides):
    for i in range(no_of_sides):
        angle=360/no_of_sides
        t.forward(100)
        t.right(angle)
for i in range(3,11):
    t.color(random.choice(colors))
    draw_shape(i)
s=Screen()
s.exitonclick()