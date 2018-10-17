def main():
    srg = input('Enter Sentence - ')
    print(deVowel(srg))
    stuffList = [10, 20, 30, 40]
    multNum = int(input('Multiply By - '))
    print(mathStuff(stuffList, multNum))


def deVowel(srg):
    newSrg = ''
    vowel = ['a', 'e', 'i', 'o', 'u']
    for x in srg:
        if x not in vowel:
            newSrg = newSrg + x
    return newSrg


def mathStuff(stuffList, multNum):
    for x in range (len(stuffList)):
        stuffList[x] *= multNum
    return stuffList


main()
