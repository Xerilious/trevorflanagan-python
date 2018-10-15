def mainFunc():
    drawSev()
    starsAndStripes()


def drawSev():
    for x in range(0,7):
        for y in range(0,7):
            print('* ',end='')
        print()


def starsAndStripes():
    for x in range(0,3):
        for y in range(0,7):
           print('*',end='')
        for z in range(0,7):
           print('-',end='')
        print()



mainFunc()
