from random import*
ROLLNUM = 2


def mainFunc():
    sideBySide()
    setOfDice = [0] * 6
    setOfDice = defineDice()


def sideBySide():
    play = 'y'
    game = 0
    while input('Play?'):
        for x in range(0, 1):
            print('~~~~', end = '')
            print(x)
            game = game + 1
            print('game - ' + str(game))


def defineDice():
    play = 1


mainFunc()
