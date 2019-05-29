def RecursiveMultiply(x,y):
    k=0
    if y<0 or x<0:
        x1 = abs(x)
        y1 = abs(y)
    else:
        x1 = x
        y1 = y
    for i in range(1, y1+1):
        k = k+x1
    if y < 0 and x < 0:
        return k
    elif y<0 or x<0:
        k = 0 - k
        return k
    else:
        return k





print(RecursiveMultiply(9,7))



