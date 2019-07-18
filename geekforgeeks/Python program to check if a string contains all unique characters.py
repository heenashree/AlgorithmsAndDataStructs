#Method 1
str = 'abcd10jk'
sort_str = sorted(str)

for i in range(len(sort_str)):
    try:
        if sort_str[i] == sort_str[i+1]:
            print("Not Unique")
            break

    except IndexError:
        pass
    #if you have reached to the end of the str
    if i == len(sort_str)-1:
        print("Unique")

#Method 2





