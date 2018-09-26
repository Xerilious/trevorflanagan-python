def mainFunction():
    print('Begin')
    schoolsubject()
    yearsInSchool()
    MyCity = input('Where Are You From? - ')
    gradeInSchool = input('How Many Years Have You Been In School? - ')
    gradeAndCity(MyCity, int(gradeInSchool))
    num1 = input('Type In Start - ')
    num2 = input('Type In End - ')
    randomNum(num1, num2)
    length = input('Type In Length - ')
    width = input('Type In Width - ')
    calculatedArea = boxArea(length, width)
    print('The Area Is ' + str(calculatedArea))
    Length = int(input('Type In Length - '))
    Width = int(input('Type In Width - '))
    calculatedPerimeter = boxPeri(Length, Width)
    print('The Perimeter Is - ' + str(calculatedPerimeter))


def schoolsubject():
    print('Bellarmine Prep')
    print('Favorite Subject Is Python')


def yearsInSchool():
    myGrade = input('Enter Your Grade - ')
    myGrade = int(myGrade)+1
    print('Your Years In School Are - ' + str(myGrade))


def gradeAndCity(city, grade):
    x = grade - 1
    print('Good Morning ' + city)
    print('You Are In ' + str(x) + 'th Grade')


from random import*

def randomNum(numA, numB):
    myNumber = randint(int(numA), int(numB))
    print(myNumber)


def boxArea(Len, Wid):
    area = int(Len) * int(Wid)
    return (area)


def boxPeri(len, wid):
    perimeter = (len * 2) + (wid * 2)
    perimeter = str(perimeter)
    return (perimeter)


mainFunction()
