#! /usr/bin/python

# e-satis @ stackoverflow: http://stackoverflow.com/questions/231767/the-python-yield-keyword-explained

# Iteration : Going over items in a list, one-by-one
print "iterators"
myList=[x*x for x in range(3)]
print myList
for i in myList: # "for X in Y" is an iteration pattern
    print i

# The retrieval of the next item using the iterator is done by calling its next() method.

print "generators"
myGenerator=(x*x for x in range(3))
# 'myGenerator' is an initerable 'generator object'
for i in myGenerator:
    print i,

for k in myGenerator:
    print k
    print 'this wont work'


print "Timing. This may take a few seconds..."
#import timeit
#print timeit.timeit('sum(xrange(200))',setup='') # uses generator
#print timeit.timeit('sum(range(200))',setup='') # does not use generator

def createGenerator():
    myList3=range(3)
    for i in myList3:
        print "->",i
        yield i*i # this function returns the generator '(i*i for i in range(3))'

myGenerator=createGenerator()
print myGenerator # 'myGenerator' is an initerable 'generator object'
for i in myGenerator:
    print i,
print


class Bank():
    crisis=False
    def create_atm(self):
        while not self.crisis:
            yield "$100"

#when everything's OK, the ATM gives you as much money as you want (each iterative withdrawls yields $100)
bank=Bank()
beforeCrisisATM=bank.create_atm()
print [beforeCrisisATM.next() for i in range(9)]
print [beforeCrisisATM for i in range(9)]
bank.crisis=True
try:
    print beforeCrisisATM.next()
except StopIteration:
    print "beforeCrisisATM threw StopIteration exception!"

# Creating a new ATM won't help, because the bank is still in crisis
duringCrisisATM=bank.create_atm()
try:
    print duringCrisisATM.next()
except StopIteration:
    print "duringCrisisATM threw StopIteration exception!"

# The trouble is, even post-crisis, the ATMs remain empty,
# because once the generator ran out for watever reason
# (e.g. due to an if/else statement such as in the Bank() case)
# there is no place for the iterator to pick up, and the generator is dead.
bank.crisis=False
try:
    print beforeCrisisATM.next()
except StopIteration:
    print "beforeCrisisATM threw StopIteration exception!"
try:
    print duringCrisisATM.next()
except StopIteration:
    print "duringCrisisATM threw StopIteration exception!"

# However, if we now build another ATM, this new one doesn't know about the past crisis
postCrisisATM=bank.create_atm()
print postCrisisATM.next()
print postCrisisATM.next()
print postCrisisATM.next()


#=====================
print



class FirstN(object):
    def __init__(self, n):
        self.n=n

    def __iter__(self):
        return self

sumOfFirstN=sum(FirstN(100))