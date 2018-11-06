from random import*
ROLLNUM = 2


def mainFunc():
    answer = findDice()
    defineDice(answer)
    print(answer)
    sideBySide()


def defineDice(answer):
    topBottom = ' ~~~~~ '
    leftOne =   '|@    |'
    middleOne = '|  @  |'
    rightOne =  '|    @|'
    aCouple =   '|@   @|'
    emptyOne =  '|     |'
    #if answer == 'snakeeyes!':
    #print(answer)
        if answer == 1:
            print(topBottom, emptyOne, middleOne, emptyOne, topBottom)
        if answer == 2:
            print(topBottom, leftOne, emptyOne, rightOne, topBottom)
        if answer == 3:
            print(topBottom, leftOne, middleOne, rightOne, topBottom)
        if answer == 4:
            print(topBottom, aCouple, emptyOne, aCouple, topBottom)
        if answer == 5:
            print(topBottom, leftOne, emptyOne, rightOne, topBottom)



def findDice():
    rollDice = randint(1, 6)
    return rollDice


def sideBySide():
    game = 0
    while input('Play?'):
        for x in range(0, 1):
            game = game + 1
            print('game - ' + str(game))



mainFunc()
