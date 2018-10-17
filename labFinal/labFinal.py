def main():
    longYear()
    num1 = [23, 70, 69, 53]
    answer = numGradeList(num1)
    print(answer)
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

def numGradeList(myNum1):
    average = 0
    for x in range(len(myNum1)):
        average += float(myNum1[x])

    #gradeAvg = (myNum1[0] + myNum1[1] + myNum1[2] + myNum1[3])/myNum2
    return average / len(myNum1)


def gradeCheck(gradeAvg):
    if gradeAvg >= 90:
        print('You Have An A')
    elif gradeAvg >= 80:
        print('You Have A B')
    elif gradeAvg >= 70:
        print('You Have A C')
    else:
        return ('Uh Oh')
    return gradeAvg


def gradeResponse(gradeCheck):
    if gradeCheck == ('Uh Oh'):
        print('Start Working!')
        input('pause')
    else:
        print('You Are Passing!')


main()
