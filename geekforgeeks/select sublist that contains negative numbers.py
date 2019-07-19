data = [[1,5], [2,-3,1], [10, -1], [-8], [10,1], [-5,4,4,-2]]
data_neg = []
#method 1
for i in data:
    for j in i:
        if j < 0:
            data_neg.append(i)
            break
print(data_neg)

#method 2

k = [i for i in data if min(i) < 0]
print(k)
