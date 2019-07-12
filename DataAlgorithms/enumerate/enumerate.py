# Python program to illustrate
# enumerate function
#Enumerate() method adds a counter to an iterable and returns it in a form of enumerate object.
#This enumerate object can then be used directly in for loops or be converted into a list of tuples using list() method.
l1 = ["eat", "sleep", "repeat"]
s1 = "geek"

# creating enumerate objects
obj1 = enumerate(l1)
obj2 = enumerate(s1)
print("enumberate object", obj1)

print "Return type:", type(obj1)
print (enumerate(l1))
print(enumerate(s1))
print(list(enumerate(l1)))

# changing start index to 2 from 0
print list(enumerate(s1, 2))
print dict(enumerate(s1))
