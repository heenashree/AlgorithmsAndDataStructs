'''
Python Program to check Armstrong Number
Given a number x, determine whether the given number is Armstrong number or not. A positive integer of n digits is called an Armstrong number of order n (order is number of digits) if.

abcd... = pow(a,n) + pow(b,n) + pow(c,n) + pow(d,n) + ....
Example:

Input : 153
Output : Yes
153 is an Armstrong number.
1*1*1 + 5*5*5 + 3*3*3 = 153

Input : 120
Output : No
120 is not a Armstrong number.
1*1*1 + 2*2*2 + 0*0*0 = 9

Input : 1634
Output : Yes
1*1*1*1 + 6*6*6*6 + 3*3*3*3 + 4*4*4*4 = 1634

'''
num = 1634
n = 3
k=1
y=0
for j in str(num):
    for i in range(len(str(num))): # since integer has no len() function, we converting this to str. Also, for armstrong number, length of the num multiplies by every number, gives armstrong nuymber
        k=k*int(j)
    y=y+k
    k=1

print(y)
if y == num:
    print("Armstrong Number")
else:
    print("Not armstrong number")

