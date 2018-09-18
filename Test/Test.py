numlist=[3,6,9,12,15,18,21,24,27,30]
print(numlist)
print(len(numlist))
print(numlist[0])
print(numlist[9])
print(numlist[0:5])
sublist=numlist[0:5]
sublist.insert(0,0)
print(sublist)
sublist.append(33)
print(sublist)
sublist1=numlist+[36]
print(sublist1)
myClasses=['Precalc','APUSH','Japanese','Pilgrim Church','American Lit','Chemistry','Python']
print(myClasses)
myClasses.remove('Pilgrim Church')
print(myClasses)
favClass=myClasses.pop(5)
print('My Favorite Class')
