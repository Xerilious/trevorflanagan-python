import turtle
pen = turtle.Pen()
#pen.speed(0)
def mainFunc():
    squareThingy()
    triangleThingy()
    pentaThingy()
    circleThingy()


def squareThingy():
    pen.pencolor('#4693ff')
    pen.penup()
    pen.setpos(-100, 100)
    pen.pendown()
    for x in range(0, 4):
        pen.backward(100)
        pen.right(90)


def triangleThingy():
    pen.pencolor('#ff3638')
    pen.penup()
    pen.setpos(100, 100)
    pen.pendown()
    for x in range(0, 3):
        pen.forward(100)
        pen.left(120)


def pentaThingy():
    pen.pencolor('#74ff47')
    pen.penup()
    pen.setpos(-100, -100)
    pen.pendown()
    for x in range(0, 5):
        pen.backward(100)
        pen.left(72)


def circleThingy():
    pen.pencolor('#3789ff')
    pen.penup()
    pen.setpos(100, -100)
    pen.pendown()
    pen.right(120)
    pen.circle(100)
mainFunc()
turtle.exitonclick()
