def mainFunc():
    myPet1 = petClass('Dog', 'Rocky', 'German Shepard')
    print(myPet1.name)
    print(myPet1.type)
    myPet1.whatIsIt()
    myPet2 = petClass('Cat', 'Mountains', 'Ragdoll')
    print(myPet2.name)
    print(myPet2.type)
    myPet2.whatIsIt()
    myCage1 = cageClass('snake')
    myCage1.whatDanger()
    myCage2 = cageClass('rat')
    myCage2.whatDanger()




class petClass:
    petType = 'Cage Free Pet'

    def __init__(self, vType, vName, vBreed):
        self.type = vType
        self.name = vName
        self.breed = vBreed

    def whatIsIt(self):
        print('My pet is a ' + self.type + ', his name is ' + self.name + ', and he is a ' + self.breed)

class cageClass:
    cageType = 'Caged Pet'

    def __init__(self, vType):
        self.type =vType


    def whatDanger(self):
        if self.type == 'snake':
            print('here')
            print('My pet is a ' + self.type + ' and he is ' + 'dangerous')
        if self.type == 'rat':
            print('My pet is a ' + self.type + ' and he is ' + 'not dangerous')


mainFunc()
