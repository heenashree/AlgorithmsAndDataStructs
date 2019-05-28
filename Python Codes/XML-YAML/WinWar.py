dict1 = {'w':4, 'p':3, 'b':2, 's':1}
dict2 = {'m':4, 'q':3, 'd':2, 'z':1}

def alphabet_war(fight):
    count, count1 = 0,0
    for i in fight:

        if i in [x for x in dict1.keys()]:
            count = count + dict1[i]
        if i in [x for x in dict2.keys()]:
            count1 = count1 + dict2[i]
    print (count, count1)

    if count > count1:
        print("")
    elif count < count1:
        print("")
    else:
        print()


"""def alphabet_war(fight):
    d = {'w':4,'p':3,'b':2,'s':1,
         'm':-4,'q':-3,'d':-2,'z':-1}
    r = sum(d[c] for c in fight if c in d)
    
    return {r==0:"Let's fight again!",
            r>0:"Left side wins!",
            r<0:"Right side wins!"
            }[True]
            """