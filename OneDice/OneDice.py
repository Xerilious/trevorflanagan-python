from random import *


def mainFunc():
    blowOnTheDice = input('Blow On The Dice?')
    roll = rollDice()
    printDice(roll)
    if blowOnTheDice == 'Y':
        mainFunc()




def rollDice():
    x = randint(1, 6)
    return x


def printDice(answer):
    diceOne = ('|     |\n|  @  |\n|     |')
    diceTwo = ('|@    |\n|     |\n|    @|')
    diceThree = ('|@    |\n|  @  |\n|    @|')
    diceFour = ('|@   @|\n|     |\n|@   @|')
    diceFive = ('|@   @|\n|  @  |\n|@   @|')
    diceSix = ('|@   @|\n|@   @|\n|@   @|')
    endLine = ('  ~~~~')
    print(endLine)
    if answer == 1:
        print(diceOne)
    if answer == 2:
        print(diceTwo)
    if answer == 3:
        print(diceThree)
    if answer == 4:
        print(diceFour)
    if answer == 5:
        print(diceFive)
    if answer == 6:
        print(diceSix)
    print(endLine)


mainFunc()
