def main():
    allInOne()


def allInOne():
    revisedCart = []
    shoppingCart = [['toothpaste', 'q-tips', 'milk'], ['milk', 'candy', 'apples'], ['paper', 'pencils', 'q-tips']]
    for subList in shoppingCart:
        #print(subList)
        for item in subList:
            #print(item)
            if item not in revisedCart:
                revisedCart.append(item)
    print(revisedCart)


main()
