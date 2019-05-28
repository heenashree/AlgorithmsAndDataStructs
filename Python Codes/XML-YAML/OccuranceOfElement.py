
def find_all(array, n):
    list1=[]
    for i in range(len(array)):
        if n == array[i]:
            list1.append(i)
    print(list1)
find_all([10, 16, 20, 6, 14, 11, 20, 2, 17, 16, 14], 16)