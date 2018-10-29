from random import *

def mainFunc():
    roll = rollDice()
    printDice(roll)


def rollDice():
    x = randint(1, 6)
    input('Snake Eyes!')
    return x


def printDice(answer):
    diceOne = ('|     |\n|  @  |\n|     |')
    diceTwo = ['|@    |', '|     |', '|    @|']
    diceThree = ['|@    |', '|  @  |', '|    @|']
    diceFour = ['|@   @|', '|     |', '|@   @|']
    diceFive = ['|@   @|', '|  @  |', '|@   @|']
    diceSix = ['|@   @|', '|@   @|', '|@   @|']
    endLine = (' ~~~~')
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

# def finalFunc():
#     input('Once More?')
#     if
mainFunc()
