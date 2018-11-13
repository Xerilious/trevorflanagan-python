import turtle
squareAngle = 90
triAngle = 60
pen = turtle.Pen()
def mainFunc():
    lineFunc()
    squareFunc(squareAngle)


def lineFunc():
    pen.forward(100)

def squareFunc(squareAngle):
    pen.penup()
    pen.forward(100)
    pen.pendown()
    for x in range(0, 4):
        pen.setx(0)
        pen.sety(0)
        pen.forward(200)
        pen.right(squareAngle)

mainFunc()
turtle.exitonclick()
