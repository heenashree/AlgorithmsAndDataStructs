import itertools
import functools

def perm(num):
    sum = 0
    num1 = list(str(num))
    for l in range(1, len(num1)+1):
        for subset in itertools.permutations(num1, l):
            print(subset)

            xyz = functools.reduce(lambda rst, d: rst * 10 + d, (list(subset)))
            print(xyz)







perm(360)