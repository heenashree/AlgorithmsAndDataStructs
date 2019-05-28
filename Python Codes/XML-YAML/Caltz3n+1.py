def collatz(n, steps):
    if(n == 1):
        return steps
    return collatz(n/2, steps+1) if n%2 ==0 else collatz(3*n+1, steps+1)


def hotpo(n):
    if n==0:
        return 0
    return collatz(n, 0)


hotpo(7)
