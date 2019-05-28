def sum_and_multiply(sum, multiply):
    for x in range(1000):
        for y in range(1000):
            if x+y == sum and x*y == multiply:
                print(x,y)
                return x,y

sum_and_multiply(12,36)