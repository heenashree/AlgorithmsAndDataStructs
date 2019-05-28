class Cat():
    def __init__(self, Animal):
        self.Animal = Animal
    def speak(self):
        print (self.Animal + " meawos")
        return (self.Animal + " meawos")


cat = Cat('Mr Whiskers')
cat.speak()
