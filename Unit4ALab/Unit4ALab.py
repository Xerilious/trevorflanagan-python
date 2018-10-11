def main():
    srg = input('Enter Sentence - ')
    print(deVowel(srg))

    mathStuff()


def deVowel(srg):
    newSrg = ''
    vowel = ['a', 'e', 'i', 'o', 'u']
    for x in srg:
        if x not in vowel:
            newSrg = newSrg + x
    return newSrg


def mathStuff(stuffList, multNum):
    stuffList == [10, 20, 30, 40]
    multNum == input('Multiply By - ')
    return 



main()
