def mainFunc():
    textCodes()


def textCodes():
    myDictionary = {'tyl':'Text You Later', 'fyi':'For Your Information', 'wya':'Where You At'}
    print(myDictionary)
    textCode = input('Whats The Code? - ')
    while textCode in myDictionary:
        print(myDictionary)
        input('Any Others?')
    else:
        mainFunc()


mainFunc()
