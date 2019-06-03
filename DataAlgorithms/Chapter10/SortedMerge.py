
# Now we can opt for merge sort, quick sort or radix sort
def MergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[mid:]
        R = arr[:mid]
        MergeSort(L)
        MergeSort(R)
        i=j=k=0
        while i < len(L) and j <len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i=i+1
            else:
                arr[k]=R[j]
                j=j+1
            k=k+1

        while i < len(L):
            arr[k] = L[i]
            
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j = j + 1
            k = k + 1
    print(arr)
A = [1,2,3,10,12]
B = [5,10,11,12]

A.extend(B)
print(A)
MergeSort(A)
