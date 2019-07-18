#How to find prime number, a prime number is only divisible by 1 and number itself
num = 6
k = [i for i in range(2,num) if num%i == 0]
print(k)
if not k:
    print("Prime number")
else:
    print("Prime")

#x= lambda(x,y in range(x) if x%y ==0 else pass)

#Method 2
nums = range(2, 100)
for i in range(2, 10):
    nums = filter(lambda x: x == i or x % i, nums)
print nums
#x == i or x % i is the same as saying x % i == 0 and x != i. When x == i, x % i will never be zero

#Method 3
from math import sqrt
for x in xrange(2,100):
    if not any(y for y in xrange(2,1+int(sqrt(x))) if not x%y):
        print x

#Method 4
k = [x for x in range(2, 20) if all(x % y != 0 for y in range(2, x))]
print(k)

#Method 5
min = 10

max = 100

primes = [num for num in range(min,max) if 0 not in [num%i for i in range(2,int(num/2)+1)]]

print (primes)