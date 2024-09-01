# Inheritance

class Animal():
    def __init__(self):
        print("Animal Created ")

    def whoAmI(self):
        print("ANIMAL")


    def eat(self):
        print('Eating')

class Dog(Animal):

    def __init__(self):
        Animal.__init__(self)
        print("Dog Created")

    def  hello(self):
        print("Hello")


mya = Dog()
mya.whoAmI()
mya.hello()

mya.eat()


