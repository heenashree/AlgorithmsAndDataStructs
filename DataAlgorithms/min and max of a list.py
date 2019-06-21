
arr=[]
#sort the array and then take first and last element as min and max

#how to sort the array, merge sort
def Msort(listy):
    if len(listy) >1:
        mid = len(listy)//2 #
        left = listy[:mid]
        print(left)
        right = listy[mid:]
        print(right)
        Msort(left)
        Msort(right)
        i=j=k=0
        while i<len(left) and j < len(right):
            if left[i]<=right[j]:
                print("i", i, left[i])
                arr[k]=left[i]
                i = i+1

            else:
                arr[k]=right[j]
                j = j+1
            k=k+1
        while i < len(left):
            arr[k] = left[i]
            i = i+1
            k= k+1
        while j <len(right):
            arr[k] = right[j]
            j = j+1
            k = k+1
    print(arr)

Msort([1,2,3,4,6,1,4,10,30,12,10])