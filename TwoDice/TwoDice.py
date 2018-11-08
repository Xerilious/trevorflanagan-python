from random import*
ROLLNUM = 2


def mainFunc():
    setOfDice = [0] * 6
    setOfDice = defineDice()
    print(setOfDice)
    sideBySide(setOfDice)
    snake = [0] * ROLLNUM
    play = input('Play? - ')
    while play == 'y':
        for i in range(0, ROLLNUM):
            num = findDice()
            snake[i] = setOfDice[num]
        sideBySide(snake)
        play = input('Play? - ')



def defineDice():
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
        elif num == 1:
            dice[num] = [topBottom, leftOne, emptyOne, rightOne, topBottom]
        elif num == 2:
            dice[num] = [topBottom, leftOne, middleOne, rightOne, topBottom]
        elif num == 3:
            dice[num] = [topBottom, aCouple, emptyOne, aCouple, topBottom]
        elif num == 4:
            dice[num] = [topBottom, leftOne, emptyOne, rightOne, topBottom]
        else:
            dice[num] = [topBottom, aCouple, aCouple, aCouple, topBottom]

    return dice



def findDice():
    num = randint(0, 5)
    return num


def sideBySide(diceSet):
    print('sidebyside')
    for row in range(0, len(diceSet[0])):
        for col in range(0, len(diceSet)):
            print(diceSet[col][row], end='\t')
        print()


mainFunc()
