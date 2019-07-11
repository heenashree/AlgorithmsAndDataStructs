'''
Python | Filter even values from a list
Given a list of numbers, the task is to make a new list containing only even values.

Examples:

Input: list = [1, 2, 3, 4, 5]
Output: [2, 4]

Input: list = [12, 14, 95, 3]
Output: [12, 14]
'''

list1 = [1, 2, 3, 4, 5]
x= [i for i in list1 if i%2==0]
print(x)

x1 = list(filter(lambda x:x%2==0, list1))

print(x1)