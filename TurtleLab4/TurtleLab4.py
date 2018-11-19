import turtle
pen = turtle.Pen()
pen.speed(0)
def mainFunc():
    creativeThingy()


def creativeThingy():
    for x in range(0, 800):
        pen.pencolor('red')
        pen.forward(100)
        pen.left(100)
        pen.pencolor('blue')
        pen.forward(100)
        pen.left(99)


mainFunc()
turtle.exitonclick()
