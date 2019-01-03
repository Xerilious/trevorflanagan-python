def mainFunc():
    print('here')

class petClass:
    petType = 'Cage Free Pet'

    def __init__(self, vType, vName, vBreed):
        self.type = vType
        self.name = vName
        self.breed = vBreed

    def whatIsIt(self):
        print('My pet is a ' + self.type + ', his name is ' + self.name + ', and he is a ' + self.breed)



    mainFunc()
