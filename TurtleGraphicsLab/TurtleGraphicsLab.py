import turtle
pen = turtle.Pen()
angle = 90
def mainFunc():
    squareDrawing(angle)
    rectangleDrawing(angle)
    circleThing()

def squareDrawing(angle):
    turtle.bgcolor("#28ff74")
    pen.pencolor("red")
    for x in range(0, 4):
        pen.forward(angle)
        pen.left(angle)
    pen.penup()
    pen.setx(100)
    pen.pendown()
    turtle.bgcolor("#8240ff")
    for x in range(0, 4):
        pen.pencolor('blue')
        pen.forward(100)
        pen.right(angle)



def rectangleDrawing(angle):
    turtle.bgcolor("#f735f2")
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
    pen.pencolor("#ff8732")
    pen.forward(150)
    pen.left(angle)
    pen.forward(100)
    pen.left(angle)
    pen.forward(150)
    pen.left(angle)
    pen.forward(100)


def circleThing():
    turtle.bgcolor("#796ff0")
    pen.penup()
    pen.right(55)
    pen.back(350)
    pen.pendown()
    pen.pencolor('pink')
    pen.circle(50)


mainFunc()
turtle.exitonclick()
