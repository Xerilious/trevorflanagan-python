#Etch-A-Sketch!
import turtle
import random
pen = turtle.Pen()
pen1 = turtle.Pen()
pen.speed(0)
pen1.speed(0)
antonia = turtle.Screen()
wn = turtle.Screen()
def mainFunc():
    pen.pencolor('red', 'yellow')
    jimBurden()


def jimBurden():
    pen.forward(10)


while True:
    pen.forward(200)
    pen.pencolor(random.randint(0, 255)/255, random.randint(0, 255)/255, random.randint(0, 255)/255)
    pen.left(178)
    antonia.onkey(jimBurden(), 'Up')
    wn.onkeypress(print('right'))


mainFunc()
#turtle.exitonclick
