def MagicIndex(arr):
    k=[i for i in range(len(arr)) if i == arr[i]]
    return k


l=[5,6,5,3,4,5,0]
print(MagicIndex(l))