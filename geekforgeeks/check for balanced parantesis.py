arr = ['(hello)', ')yellow(', '((', ')', 'le()ft']

def is_balanced(arr):
    count = 0
    for i in arr:
        if i == '(':
            count = count+1
        elif i == ')':
            count = count -1
    if count < 0:
        print(count)
        return 'false'
    #if count == 0:
    #    print(count)
    #    return 'True'
    return count == 0
print(is_balanced(arr))

