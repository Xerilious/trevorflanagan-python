#Etch-A-Sketch!
import turtle
import random
pen = turtle.Pen()
pen.speed(0)
def mainFunc():
    pen.pencolor('red', 'yellow')
while True:
    pen.forward(200)
    pen.pencolor(random.randint(0, 255)/255, random.randint(0, 255)/255, random.randint(0, 255)/255)
    pen.left(178)


mainFunc()
turtle.exitonclick
