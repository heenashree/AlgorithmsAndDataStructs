'''
A = [10,11,12,13,14,1,2,3,4]
num = 4

if num in A:
    print(A.index(num))
'''


'''
A = [10,11,12,13,14,1,2,3,4]
num = 17
x= len(A)
def RotatedArray(A, l, x, num):
    if len(A) > 1:
        return -1
    mid = len(A)//2
    L = A[mid:]
    R= A[:mid]
    if A[mid]== num:
        return mid
    if A[1]<=A[mid]: # this means the fisrt half is sorted
        if num >=A[mid] and num <= A[mid]:
            return RotatedArray(A,1,mid-1,num)
        return RotatedArray(A,mid+1, len(A), num)
        if key >= arr[mid] and key <= arr[h]:
            return search(a, mid+1, h, key)
        return search(arr, l, mid-1, key)


def RotatedArray(A, 0, x, num):
'''


RotatedArray(A)

