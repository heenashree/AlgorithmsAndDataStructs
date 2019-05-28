dict_items = {1:'one', 2:'two', 3:'three',4:'four',5:'five', 6:'six',7:'seven',8:'eight',9:'nine',0:'zero'}
number = {'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9, 'zero':0}
import re

def numToWord(n):
    z2 = ""
    for i in str(n):
        for k, v in dict_items.items():
            if str(k) == i:
                z2 = z2 + dict_items[k]
    print("convert number to word", z2)

    return z2

def toDigit(z1):
    z2 = ""
    for k, v in number.items():
        try:
            z4 = re.findall(k, z1)
            for i in range(len(z4)+1):
                if k == z4[i]:
                    zy = number[k]
                    z2 = str(z2) + str(zy)
        except:
            pass
    print("convert word to number", z2)
    return z2




list1 = []

def numbers_of_letters(n):
    print("Entry point", n)
    z = numToWord(n)
    list1.append(z)
    lenNum = len(z)
    print("z leng and z value", lenNum, z)

    if lenNum < 10:
        list1.append(numToWord(lenNum))
        print(list1)
    elif lenNum > 10:
        z1 = numToWord(lenNum)
        print("z1", z1)
        print(list1)
    z1 = toDigit(z1)
    print("type of z1", type(z1))
    if lenNum == n:
        exit()
    numbers_of_letters(int(z1))



#numbers_of_letters(12) #, ["threeseven", "onezero", "seven", "five", "four"])
numbers_of_letters(311) #, ['threeoneone', 'oneone', 'six', 'three', 'five', 'four'])
#numbers_of_letters(999) #, ["nineninenine", "onetwo", "six", "three", "five", "four"])