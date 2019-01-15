#Etch-A-Sketch!
import turtle
import random
pen = turtle.Pen()
pen1 = turtle.Pen()
pen.speed(0)
wn = turtle.Screen()
running = True


def mainFunc():
    instructionSheet()
    upFunc()
    downFunc()
    rightFunc()
    leftFunc()
    downLeft()
    update()


def instructionSheet():
    pen1.up()
    pen1.goto(-300, 250)
    pen1.down()
    pen1.write('ETCH-A-SKETCH!', font=("Arial", 20, "normal"))
    pen1.forward(250)
    pen1.up()
    pen1.goto(-275, 225)
    pen1.down()
    pen1.write('-Use Arrow Keys to Move On X and Y Axis', font=('Arial', 16, 'normal'))
    pen1.up()
    pen1.goto(-275, 200)
    pen1.down()
    pen1.write('-Use s, d, a, and f For Diagonal Movement', font=('Arial', 16, 'normal'))
    pen1.up()
    pen1.goto(-275, 175)
    pen1.down()
    pen1.write('-Draw Something Before Time Runs Out!', font=('Arial', 16, 'normal'))


def upFunc():
    pen.up()
    pen.setheading(90)
    pen.down()
    pen.forward(10)


def downFunc():
    pen.up()
    pen.setheading(270)
    pen.down()
    pen.forward(10)


def leftFunc():
    pen.up()
    pen.setheading(180)
    pen.down()
    pen.forward(10)


def rightFunc():
    pen.up()
    pen.setheading(0)
    pen.down()
    pen.forward(10)


def downLeft():
    pen.up()
    pen.setheading(225)
    pen.down()
    pen.forward(10)


def downRight():
    pen.up()
    pen.setheading(315)
    pen.down()
    pen.forward(10)


def upLeft():
    pen.up()
    pen.setheading(135)
    pen.down()
    pen.forward(10)


def upRight():
    pen.up()
    pen.setheading(45)
    pen.down()
    pen.forward(10)


def update():
    while running == True:
        pen.pencolor(random.randint(0, 255)/255, random.randint(0, 255)/255, random.randint(0, 255)/255)
        update()


wn.onkey(upFunc, "Up")
wn.onkey(downFunc, "Down")
wn.onkey(leftFunc, "Left")
wn.onkey(rightFunc, "Right")
wn.onkey(downLeft, "s")
wn.onkey(downRight, "d")
wn.onkey(upLeft, "a")
wn.onkey(upRight, "f")
wn.listen()
mainFunc()
update()
