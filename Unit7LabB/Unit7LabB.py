def mainFunc():
    print('here')
    myPet1 = pet('Jemma', 'Australian Labradoodle')
    print(myPet1.name)
    print(myPet1.breed)
    myPet2 = dog('Loki', 'Australian Labradoodle', 'Tan')
    print(myPet2.name)
    print(myPet2.breed)
    print(myPet2.color)
    myPet1.whatIsIt()
    myPet2.whyIsIt()


class pet:

    def __init__(self, vName, vBreed):
        self.name = vName
        self.breed = vBreed

    def whatIsIt(self):
        print("My pet's name is " + self.name + ', and he is a ' + self.breed)


class dog(pet):
    def __init__(self, vName, vBreed, vColor):
        pet.__init__(self, vName, vBreed)
        self.color = vColor


    def whyIsIt(self):
        print("My pet's name is " + self.name + ', and he is a ' + self.breed + ', he is ' + self.color)

    #def __init__(self, vName, vBreed):
        #parentClass.__init__(self, vName, vBreed)
        #self.name = vName
        #self.breed = vBreed


mainFunc()
