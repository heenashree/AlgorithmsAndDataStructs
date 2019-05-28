class Person:
    def __init__(self, name, age):
        self.info= name + "age is " + str(age)
    def result(self):
        print(self.info)
        return self.info



names=["john","matt","alex","cam"]
ages=[16,25,57,39]
for i in range(4):
    name,age = names[i],ages[i]
    person = Person(name,age)
    z = person.info
