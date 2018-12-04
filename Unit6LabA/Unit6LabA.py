def mainFunc():
    textCodes()


def textCodes():
    myDictionary = {'tyl':'Text You Later', 'fyi':'For Your Information', 'wya':'Where You At'}
    x = 1
    while x == 1:
        print(myDictionary)
        textCode = input('Whats The Code? - ')
        if textCode in myDictionary:
            print('Perfection')
        else:
            myDictionary[textCode] = input('Nani Kore? - ')


mainFunc()
