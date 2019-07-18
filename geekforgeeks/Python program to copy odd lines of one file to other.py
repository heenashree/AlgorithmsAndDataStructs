#Method 1
with open('test', 'r') as f:
    for i,l in enumerate(f,2):
        print (i,l)
        if i%2 == 1:
            print(i)
            with open('testOdd', 'a+') as fOdd:
                fOdd.write(l)


