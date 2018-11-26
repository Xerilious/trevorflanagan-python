import turtle
pen = turtle.Pen()
pen.speed(0)
def mainFunc():
    creativeThingy()
    rosetteThingy()


def creativeThingy():
    for x in range(0, 50):
        pen.pencolor('red')
        pen.forward(100)
        pen.left(100)
        pen.pencolor('blue')
        pen.forward(100)
        pen.left(168)


def rosetteThingy():
    for x in range(0, 119):
        pen.pencolor('#748ff9')
        pen.circle(50)
        pen.left(47)
        pen.pencolor('#f928f2')
        pen.circle(100)
        pen.left(87)
        pen.pencolor('#ff1429')
        pen.circle(25)



mainFunc()
turtle.exitonclick()
