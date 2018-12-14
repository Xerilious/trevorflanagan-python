def mainFunc():
    print('Gaaaddd Daaammmmiiittt!')
    myPet1 = petClass('Dog', 'Rocky', 'German Shepard')
    print(myPet1.name)
    print(myPet1.type)
    myPet1.whatIsIt()
    myPet2 = petClass('Cat', 'Mountains', 'Ragdoll')
    print(myPet2.name)
    print(myPet2.type)
    myPet2.whatIsIt()




class petClass:
    petType = 'Cage Free Pet'

    def __init__(self, vType, vName, vBreed):
        self.type = vType
        self.name = vName
        self.breed = vBreed

    def whatIsIt(self):
        print('My pet is a ' + self.type + ', his name is ' + self.name + ', and he is a '+ self.breed)

class cageClass:
    cageType = 'Caged Pet'

    def __init__(self, vType, vName, vBreed):
        self.type =vType
        self.name = vName
        self.breed = vBreed

    def whatDanger(self):
        pass











mainFunc()
