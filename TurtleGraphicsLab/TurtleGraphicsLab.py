import turtle
pen = turtle.Pen()
angle = 90
def mainFunc():
    squareDrawing(angle)
    rectangleDrawing(angle)

def squareDrawing(angle):
    pen.pencolor("red")
    for x in range(0, 4):
        pen.forward(angle)
        pen.left(angle)
    pen.penup()
    pen.setx(100)
    pen.pendown()
    for x in range(0, 4):
        pen.pencolor('blue')
        pen.forward(100)
        pen.right(angle)


def rectangleDrawing(angle):
    pen.pencolor('green')
    pen.penup()
    pen.setx(-200)
    pen.pendown()
    pen.forward(120)
    pen.left(angle)
    pen.forward(30)
    pen.left(angle)
    pen.forward(120)
    pen.left(angle)
    pen.forward(30)
    turtle.bgcolor('black')
    pen.penup()
    pen.sety(200)
    pen.pendown()
    pen.pencolor('yellow')
    pen.forward(150)
    pen.left(angle)
    pen.forward(100)
    pen.left(angle)
    pen.forward(150)
    pen.left(angle)
    pen.forward(100)



mainFunc()
turtle.exitonclick()
