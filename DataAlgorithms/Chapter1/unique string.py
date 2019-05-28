'''def unique(val):
   k = [i for i in val]
   print (k)
   for i in range(len(k)):
       for j in range(i+1, len(k)):
           if k[i] == k[j] :
               return ("not")
   return("yes")
print(unique('weds=vc'))
Time complexity = O(n**2)
'''

'''

Time - O(n)
def isUniqueChars(st):

	# String length cannot be more than
	# 256.
	if len(st) > 256:
		return False

	# Initialize occurrences of all characters
	char_set = [False] * 128

	# For every character, check if it exists
	# in char_set
	for i in range(0, len(st)):

		# Find ASCII value and check if it
		# exists in set.
        print(i)
		val = ord(st[i])
        print(val)
		if char_set[val]:
			return False

		char_set[val] = True

	return True

# driver code
st = "abcd"
print(isUniqueChars(st))
'''


'''
#Using Sorting Method

def unique(str):
    str1 = sorted(str)
    for i in range(len(str1)-1):
        if str1[i] == str1[i+1]:
            return False
    return True


print(unique('helwewo'))
Complexit = O(nlogn)
'''
