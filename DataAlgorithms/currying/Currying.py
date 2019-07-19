#Currying is a term from functional oriented programming. It is refered to the functions that return other functions.

def a(x):
    def b(y):
        return x*y
    return b

result = a(3)(4)
print(result)

addr_4 = a(4)
addr_10 = a(10)

print(addr_4(3))  # a(4)(3) #12
print(addr_10(4)) # a(10)(4) # 40

