x = [1,3,5,6,10, 12, 2]
a = min(x)
b = max(x)

imin = x.index(min(x))
imax = x.index(max(x))
print(imin, imax)
x[imin] = b
x[imax] = a

print(x)