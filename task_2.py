from turtle import forward, speed, exitonclick,backward, left, pendown, penup, goto
from random import randint
speed("normal")
penup()
goto(-270,-200)
pendown()
def rectangle(x,y):
    for _ in range(2):
        backward(x)
        left(90)
        forward(y)
        left (90)
def gap():
    penup()
    forward(30)
    pendown()
for _ in range(20):
    rectangle(20, randint(30, 220))
    gap()
exitonclick()
