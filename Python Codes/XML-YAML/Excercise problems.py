#Example 1
print(unichr(1234))
#output 1234

#Example 2
a = 10
b = 2
print a if b else 0
#output 10

#Example 3
def addItem(listParam):
    listParam += [1]

mylist = [1, 2, 3, 4]
addItem(mylist)
print len(mylist)
#Output 5

#Example 4
def myfunc(x, y, z, a):
    print x + y
nums = [1, 2, 3, 4]
myfunc(*nums)
#output 3

#Example 5
name = 'python'
#print(bool(name))
while bool(name) == False:
    print('hi')
# It prints nothing

#Example 6
if False:
    print('Hi')
elif True:
    print('Hello')
else:
    print('Howdy')

#Output True

#Example 7
var = 100
if ( var == 100 ) :
    print "Value of expression is 100"
#output "Value of expression is 100

#Example 8
values = [1, 2, 1, 3]
nums = set(values)  #[1,2,3]
def checkit(num):
    if num in nums:
        return True
    else:
        return False
for i in filter(checkit, values):
     print i
#output
# 1,
# 2,
# 1,
# 3

#Example 9
a = range(5)
print(a)
b = range(10)
print(zip(a,b))
#output [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)]

def dostuff(param1, *param2):
    print type(param2)
    print(param1)
    print(param2)
dostuff('apples', 'bananas', 'cherry', 'dates')
dostuff('apples', ['bananas', 'cherry', 'dates'])


print "hello" 'world'


num1 = 5
if num1 >= 91:
    num2 = 3
else:
    if num1 < 6:
        num2 = 4
    else:
        num2 = 2
        x = num2 * num1 + 1
        print (x,x%7)


name = "snow storm"
name[5] = 'X'