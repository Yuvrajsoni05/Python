class Circle():
    pi = 3.14

    def __init__(self,radius = 1):
        self.radius = radius

    def area(self):
        return self.radius*self.radius * Circle.pi

    def set_radius(self,new_r):
        self.radius = new_r




x = Circle(3)
print(x.radius)
print(x.area())
x.radius = 100

x.set_radius(999)

print(x.area())

