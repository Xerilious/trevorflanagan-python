def main():
    srg = input('Enter Sentence - ')
    deVowel(srg)


def deVowel(srg):
    newSrg = ''
    vowel = ['a', 'e', 'i', 'o', 'u']
    for x in srg:
        if x in vowel:
            print(x)
    return newSrg


main()
