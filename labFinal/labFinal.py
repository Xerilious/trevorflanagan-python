def main():
    longYear()
    num1 = [50, 70, 50.3, 20.7]
    num2 = len(num1)
    print(num1)
    answer = numGradeList(num1, num2)
    process = gradeCheck(answer)
    gradeResponse(process)

def longYear():
    shortYear = int(input('Type In Year - '))
    if shortYear == 9:
        print ('Freshmen')
    elif shortYear == 10:
        print ('Sophmore')
    elif shortYear == 11:
        print ('Junior')
    elif shortYear == 12:
        print ('Senior')
    else:
        print('You Should Not Be Here')

def numGradeList(myNum1, myNum2):
    gradeAvg = (myNum1[0] + myNum1[1] + myNum1[2] + myNum1[3])/myNum2
    return gradeAvg


def gradeCheck(gradeAvg):
    if gradeAvg >= 90:
        print('A')
    elif gradeAvg >= 80:
        print('B')
    elif gradeAvg >= 70:
        print('C')
    else:
        print('Uh Oh')
    return gradeCheck


def gradeResponse(gradeCheck):
    print(gradeCheck)
    if gradeCheck == 'A' or 'B' or 'C':
        print('You Are Passing!')
    else:
        print('Start Working!')
    return gradeCheck



main()
