'''
The original list : ['apple', 'oranges', 'mango', 'grapes']
The list without suffix s : ['apple', 'mango']
The list with suffix s : ['oranges', 'grapes']
'''
listy=['apple', 'oranges', 'mango', 'grapes']
K=[]

#first Method
for i in listy:
    if i[-1] == 's':
        K.append(i)
print(K)


#Second Method / List comprehension
K = [i for i in listy if i[-1] == 's']
print(K)

#Third Method
end_letter = 's'
with_s = [x for x in listy if x.endswith(end_letter)]
without_s = [x for x in listy if x not in with_s]



