def mainFunction():
    #schoolsubject()
    #yearsInSchool()
    #gradeAndCity()
    #randomNum()
    #boxArea()
    boxPeri()


def schoolsubject():
    print('Bellarmine Prep')
    print('Favorite Subject Is Python')
#schoolsubject()


def yearsInSchool(grade):
    grade=int(grade)


myGrade = input('Enter Your Grade - ')
myGrade = int(myGrade)+1
print('Your Years In School Are - ' + str(myGrade))
yearsInSchool(grade=myGrade)

def gradeAndCity(city, grade):
    x = grade - 1
    print('Good Morning ' + city)
    print('You Are In ' + str(x) + 'th Grade')


MyCity = input('Where Are You From? - ')
MyGrade = input('How Many Years Have You Been In School? - ')
gradeAndCity(MyCity, int(MyGrade))

from random import*

def randomNum():
    num1 = input('Type In Start - ')
    num2 = input('Type In End - ')
    myNumber = randint(int(num1), int(num2))
    print(myNumber)
    return (myNumber)
randomNum()


def boxArea():
    length = input('Type In Length - ')
    width = input('Type In Width - ')
    area = int(length) * int(width)
    print('The Area Is ' + str(area))
    return (area)
boxArea()


def boxPeri():
    length = input('Type In Length - ')
    width = input('Type In Width - ')
    perimeter = int(length * 2) + int(width * 2)
    return ('The Perimeter Is - ' + perimeter)
boxPeri()
