import math


class Circle:
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius**2
    def perimeter(self):
        return 2 * 3.14 * self.radius


c1 = Circle(23)
print(c1.area())
print(c1.perimeter())


class Employee:
    def __init__(self,role,department):
        self.role = role
        self.department = department

    def show(self):
        print(self.role)
        print(self.department)

class Engineer(Employee):
    def __init__(self,name,age):
        self.name = name
        self.age = age
        super().__init__("IT","Tech")


s1 = Engineer("yuvraj",12)
s1.show()
print(s1.name)


class Order:
    def __init__(self,item,price):
        self.item = item
        self.price = price
    def __gt__(self,ord2):
        return self.price > ord2.price


ord1 = Order("D",23)
print(ord1.item)
print(ord1.price)
ord2 = Order("s",24)
print(ord2.item)
print(ord2.price)
print(ord1 < ord2)
