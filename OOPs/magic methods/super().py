class Foo(object):
    def __new__(cls, *args, **kwargs):
        print "Creating Instance"
        instance = super(Foo, cls).__new__(cls, *args, **kwargs)
        return instance

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def bar(self):
        pass

a = Foo(2,3)
