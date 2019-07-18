# we know the arr is sorted
def binarySearch(arr1,num):
    if len(arr1) >1:
        mid = len(arr1)//2

        if num == arr1[mid]:
            print mid
            return arr1[mid]
        elif num > arr1[mid]:

            binarySearch(arr1[mid:],num)
        else:

            binarySearch(arr1[:mid], num)


arr1 = [2,3,4,5,6,7]
num = 4
binarySearch(arr1, num)