#Given two sorted arrays arr1[] and arr2[] in non-decreasing order with size n and m. The task is to merge the two sorted arrays into one sorted array (in non-decreasing order).

arr1=[0,2,3,5,6]
arr2=[3,7,8,9]
arr3=[]
print(id(arr1))
arr1.extend(arr2)
print(arr1)
print(id(arr1)) #since id is same, we are not using any more space
