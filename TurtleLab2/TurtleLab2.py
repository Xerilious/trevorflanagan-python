import turtle
import math
pen = turtle.Pen()

def mainFunc():
    someShape()


def someShape():
    pen.pencolor('black')
    x = input('Side Length - ')
    y = input('How Many Sides - ')
    z = input('What Color - ')
    total = 360.0
    pen.pencolor(z)
    angle = total/float(y)
    print(angle)
    for a in range(int(y)):
        if y > str(4):
            radius = float(x * 180)/math.pi
        pen.left(int(angle))
        pen.forward(int(x))

mainFunc()
turtle.exitonclick()
