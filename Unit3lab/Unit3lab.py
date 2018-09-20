def schoolsubject():
    print('Bellarmine Prep')
    print('Favorite Subject Is Python')
schoolsubject()


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
