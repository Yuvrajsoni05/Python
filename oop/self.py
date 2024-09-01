class Emp:
    def printdetail(self):
        return f"Name is {self.name}.Age {self.age}"


Yuvraj = Emp()
Yuvraj.name = 'Yash'
Yuvraj.Age = 23


print(Yuvraj.printdetail())
