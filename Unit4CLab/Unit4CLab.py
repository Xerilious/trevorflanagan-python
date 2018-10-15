def mainFunc():
    drawSev()
    starsAndStripes()
    incTri()


def drawSev():
    for x in range(0,7):
        for y in range(0,7):
            print('* ',end='')
        print()
    print()


def starsAndStripes():
    for x in range(0, 3):
        for y in range(0, 7):
            print('* ', end='')
        print('')
        for z in range(0,7):
            print('- ', end='')
        print()

def incTri():
    z = 0
    for x in range(0, 7):
        z = z + 1
        print('')
        for y in range(0, z):
            print(z, end='')


mainFunc()
