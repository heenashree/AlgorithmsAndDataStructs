#geekforgeeks
print type(type(int))
print(type(int))
print(int)
#Explanation: The type() function returns the class of the argument the object belongs to.
# Thus, type(int) returns which is of the type 'type' object.


print(chr(ord('A')))
#Explanation: ord() function converts a character into its ASCII notation and chr() converts the ASCII to character.

x = 'py' 'thon'

#Prints python

print(id(int))

#Explanation: ord() function converts a character into its ASCII notation and chr() converts the ASCII to character.

y = 8
z = lambda x : x * y
print z(6)
#output is 48
# Explanation: lambdas are concise functions and thus, result = 6 * 8
import time
print(time.time())