def main():
    allInOne()
    print(shoppingCart)
    countQTips()


def allInOne():
    revisedCart = []
    shoppingCart = [['toothpaste', 'q-tips', 'milk'], ['milk', 'candy', 'apples'], ['paper', 'pencils', 'q-tips']]
    for subList in shoppingCart:
        for item in subList:
            if item not in revisedCart:
                revisedCart.append(item)
    print(revisedCart)
    return shoppingCart


def countQTips(shoppingCart):
    onlyQTips = []
    for sublist in shoppingCart:
        for qTipNum in sublist:
            if qTipNum in onlyQTips:
                onlyQTips.append(qTipNum)
    print(onlyQTips)


main()
