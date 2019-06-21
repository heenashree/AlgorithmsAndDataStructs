class A:
    def f(self):
        print("in A")
        return self.g()

    def g(self):
        return 'A'

class B(A):
    def f(self):
        print("in B")
        return self.g()

    def g(self):
        return 'B'

a = A()
b = B()
print (a.f(), b.f())
print (a.g(), b.g())

#output
# A, B
# A, B