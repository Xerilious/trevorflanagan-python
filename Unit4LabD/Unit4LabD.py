def main():
    totalCart = allInOne()
    countQTips(totalCart)


def allInOne():
    totalCart = []
    revisedCart = []
    shoppingCart = [['toothpaste', 'q-tips', 'milk'], ['milk', 'candy', 'apples'], ['paper', 'pencils', 'q-tips']]
    for subList in shoppingCart:
        for item in subList:
            totalCart.append(item)
            if item not in revisedCart:
                revisedCart.append(item)
    print(revisedCart)
    #print(totalCart)
    return totalCart


def countQTips(totalCart):
    count = 0
    for sublist in totalCart:
            if sublist == 'q-tips':
                count += 1
    print(count)


main()
