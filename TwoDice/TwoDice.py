from random import*
ROLLNUM = 2


def mainFunc():
    setOfDice = [0] * 6
    #setOfDice = defineDice(num)
    num = findDice()
    defineDice(num)
    setOfDice = defineDice(num)
    print(num)
    sideBySide()


def defineDice(num):
    dice = [0] * 6
    topBottom = ' ~~~~~ '
    leftOne =   '|@    |'
    middleOne = '|  @  |'
    rightOne =  '|    @|'
    aCouple =   '|@   @|'
    emptyOne =  '|     |'
    for num in range(0, 6):
        if num == 0:
            dice[num] = [topBottom, emptyOne, middleOne, emptyOne, topBottom]
        elif dice[num] == 1:
            dice[num] = [topBottom, leftOne, emptyOne, rightOne, topBottom]
        elif dice[num] == 2:
            dice[num] = [topBottom, leftOne, middleOne, rightOne, topBottom]
        elif dice[num] == 3:
            dice[num] = [topBottom, aCouple, emptyOne, aCouple, topBottom]
        elif dice[num] == 4:
            dice[num] = [topBottom, leftOne, emptyOne, rightOne, topBottom]
        else:
            dice[num] = [topBottom, aCouple, aCouple, aCouple, topBottom]
    print(dice)

    return dice



def findDice():
    num = randint(1, 6)
    return num


def sideBySide():
    game = 0
    while input('Play?'):
        for x in range(0, 1):
            game = game + 1
            print('game - ' + str(game))



mainFunc()
