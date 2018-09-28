def main():
    longYear()
    num1 = [86.5, 75.3, 98.9, 92.3]
    num2 = len(num1)
    numGradeList(num1, num2)
    avgGrade = 
    if avgGrade >= 90:
        print('You Are Passing!')
    elif avgGrade >= 80:
        print('You Are Passing!')
    elif avgGrade >= 70:
        print('Barely Passing!')
    else:
        print('Start Working!')
    gradeCheck()

def longYear():
    shortYear = int(input('Type In Year - '))
    if shortYear < 10:
        print ('Freshmen')
    elif shortYear < 11:
        print ('Sophmore')
    elif shortYear < 12:
        print ('Junior')
    elif shortYear < 13:
        print ('Senior')

def numGradeList(myNum1, myNum2):
    print(myNum1)
    gradeAvg = (myNum1[0] + myNum1[1] + myNum1[2] + myNum1[3])/myNum2
    return gradeAvg


def gradeCheck():




main()
