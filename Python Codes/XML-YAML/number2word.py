from num2words import num2words
from word2number import w2n
import re
list1 =[]

number = {'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9}


def countNums(n):
    z =""
    list1 = [int(i) for i in str(n)]
    for i in range(1, len(list1) +1):
        z = z + num2words(i)
    k = test(z)
    return z

def test(z):
    z2 = ""
    for k,v in number.items():
        #print("test", k , z)
        try:
            z4 = re.findall(k,z)
            if z4:
                z1 = number[k]
                z2 = str(z2)+str(z1)
        except:
            pass
    return z2


def numbers_of_letters(z):
        list1.append(z)
        print("FINALLE list", list1)
        i = len(str(z))
        try:
            final = w2n.word_to_num(z)
            print("try", final)
        except ValueError:
            final = int(test(z))
            print("except", final)
        if i == final:
            exit()
        for k,v in number.items():
            if number[k] == i:
                i = num2words(i)
            else:
                i = test(final)
        numbers_of_letters(i)



#numbers_of_letters(1) #, ["one", "three", "five", "four"])
z = countNums(999)
numbers_of_letters(z) #, ["onetwo", "six", "three", "five", "four"])

