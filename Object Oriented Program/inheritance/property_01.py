class Student:
    def __init__(self,phy,math):
        self.math = math
        self.phy = phy
        # self.total = self.math + self.phy
    @property
    def total(self):
        return self.math + self.phy




s1 = Student(23,33)
print(s1.total)

s1.phy = 22
print(s1.total)

