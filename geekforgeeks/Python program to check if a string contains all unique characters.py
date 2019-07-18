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
def uniqueCharacters(str):
    # If at any time we encounter 2
    # same characters, return false
    for i in range(len(str)):
        for j in range(i + 1, len(str)):
            if (str[i] == str[j]):
                return False;

                # If no duplicate characters
    # encountered, return true
    return True;


# Driver Code
str = "GeeksforGeeks";

if (uniqueCharacters(str)):
    print("The String ", str, " has all unique characters");
else:
    print("The String ", str, " has duplicate characters");





