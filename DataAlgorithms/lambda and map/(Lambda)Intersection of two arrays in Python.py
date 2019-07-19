'''
Given two arrays, find their intersection.

Examples:

Input:  arr1[] = [1, 3, 4, 5, 7]
        arr2[] = [2, 3, 5, 6]
Output: Intersection : [3, 5]
'''

arr1 = [1, 3, 4, 5, 7]
arr2 = [2, 3, 5, 6]
arr3 = []

for i in arr1:
    if i in arr2:
        arr3.append(i)
print(arr3)

arr4 = [i for i in arr1 if i in arr2]
print(arr4)

arr5 = list(filter(lambda x: x in arr1, arr2))
print(arr5)