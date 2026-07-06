class Person:
    __name = "Yuvraj"

    def __home(self):
        print("Home")

    def welcome(self):
        self.__home()

p1 = Person()
print(p1.welcome())
