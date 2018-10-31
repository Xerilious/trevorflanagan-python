from random import *


def mainFunc():
    roll = rollDice()
    answer = printDice(roll)
    blowOnTheDice = input('Blow On The Dice?')
    while blowOnTheDice == 'of course!':
        roll = rollDice()
        printDice(roll)
        input('Again?')
        if not 'of course!':
            end()
        return blowOnTheDice


def rollDice():
    x = randint(1, 6)
    input('Snake Eyes!')
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
    return printDice(answer)


def end(blowOnTheDice):
    if blowOnTheDice == 'of course!':

        #mainFunc()
    elif not blowOnTheDice == 'of course!':
        mainFunc()



mainFunc()
