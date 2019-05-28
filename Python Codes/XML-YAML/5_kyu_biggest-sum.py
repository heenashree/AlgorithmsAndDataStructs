import time
time.sleep()

matrix = [[20, 20, 10, 10],
          [10, 20, 10, 10],
          [10, 20, 20, 20],
          [10, 10, 10, 20]]



def find_sum(m):
    sick = []

    for i in m:
        print sorted(i)
        sick.append(max(i))
        i.remove(max(i))
        print("**",i)


find_sum(matrix)
#find_sum(matrix), 140, "Testing Matrix 1")