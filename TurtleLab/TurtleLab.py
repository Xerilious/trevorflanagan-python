import turtle
squareAngle = 90
pen = turtle.Pen()
turtle.setup(width = 800, height = 800)
turtle.speed(0)

def mainFunc():
    lineFunc()
    squareFunc(squareAngle)
    triangleFunc()
    circleThingy()


def lineFunc():
    pen.setx(-50)
    pen.forward(100)
    turtle.bgcolor("#ff7648")
    pen.pencolor('red')

def squareFunc(squareAngle):
    turtle.bgcolor('#7480ff')
    pen.setx(0)
    pen.sety(0)
    pen.penup()
    pen.forward(100)
    pen.down()
    pen.right(squareAngle)
    pen.forward(100)
    for x in range(0, 4):
        pen.right(squareAngle)
        pen.forward(200)
    pen.pencolor("#ff3795")


def circleThingy():
    pen.pencolor('#f9984f')
    turtle.bgcolor("#736ff6")
    pen.penup()
    pen.setpos(-300, 0)
    pen.pendown()
    pen.circle(300)

def triangleFunc():
    turtle.bgcolor("#123456")
    pen.penup()
    pen.setx(125)
    pen.sety(200)
    # pen.left(180)
    # pen.forward(100)
    # pen.right(90)
    # pen.forward(200)
    # pen.left(180)
    #pen.left(120)
    pen.pendown()
    for x in range(0, 3):
        pen.forward(400)
        pen.right(120)





mainFunc()
turtle.exitonclick()
