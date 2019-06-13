'''
def fibo(num):
    l = [0,1]
    for i in range(2,10):
        l.append(l[i-1]+l[i-2])
    print(l)

fibo(8)
Time Complexty = O(n)
'''

#using Lambda and Reduce

from functools import reduce

fib = lambda n: reduce(lambda x, _: x + [x[-1] + x[-2]],
                       range(n - 2), [0, 1])

print(fib(5))

#using map and Lambda
def fibonacci(count):
    fib_list = [0, 1]

    any(map(lambda _: fib_list.append(sum(fib_list[-2:])),
            range(2, count)))

    return fib_list[:count]


print(fibonacci(10))