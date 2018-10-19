def main():
    loopList = [1, 2, 3, 4, 5]
    forLoopPrac(loopList)
    loopWithRange()


def forLoopPrac(loopList):
    for x in loopList:
        print(x, '+ 10 =', (x + 10))
        print(x, '* 10 =', (x * 10))


def loopWithRange():
    #rangeListAfter = ''
    rangeList = [10, 20, 30, 40, 50]
    for x in range(0, len(rangeList)):
            rangeList[x] = rangeList[x] * 10
    print(rangeList)



main()
