#Given an array of N values. Print the number which has maximum number of zeroes. If there are no zeroes then print -1.

arr = [10,100,1000,1000, 2000200]
d = {}
count = 0
for i in arr:
     for k in str(i):
         if k == '0':
             count = count+1
             d[i] = count
     count = 0
print(sorted(d.items(), key=lambda x: x[1]))
