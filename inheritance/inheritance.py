class Father:
    def Rs(self):
        print("Having 50000 Rs")
class Son(Father):

    def Money(self):
        print("Son have 5000")

obj = Son()
obj.Money()
obj.Rs()
