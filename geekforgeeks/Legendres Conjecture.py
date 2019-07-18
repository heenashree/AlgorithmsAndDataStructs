
#Conjecture: A conjecture is a proposition or conclusion based upon incompleate information to which no proof has been found i.e it has not been proved or disproved.

#Mathematically,there is always one prime p in the range n^2 to (n + 1)^2 where n is any natural number.
#for examples-
#2 and 3 are the primes in the range 1^2 to 2^2.
#5 and 7 are the primes in the range 2^2 to 3^2.
#11 and 13 are the primes in the range 3^2 to 4^2.
#17 and 19 are the primes in the range 4^2 to 5^2.
#Examples:
#Input : 4
#output: Primes in the range 16 and 25 are:
#        17
#        19
#        23

#Explanation: Here 42 = 16 and 52 = 25
#Hence, prime numbers between 16 and 25 are 17, 19 and 23.

num = input()
num1 = num+1


zee= [k for k in range(num*num, num1*num1) if all(k%i != 0 for i in range(1,k))]
print zee