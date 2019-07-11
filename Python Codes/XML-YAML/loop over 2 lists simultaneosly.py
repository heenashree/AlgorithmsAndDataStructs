

import math

count = 0
x = 80
y = 90
def isPerfectSquare(x, count =0):

    for i in range(x+1, y):
        sr = math.sqrt(i)
        print("sr", sr)
        print(math.floor(sr))
        if(sr - math.floor(sr)) == 0:
            count = count+1

            isPerfectSquare(int(sr), count)
        else:
            x = x+1





isPerfectSquare(x)


