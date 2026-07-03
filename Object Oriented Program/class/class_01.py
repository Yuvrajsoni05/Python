class Student:
    college_name = "ABC Collage"
    name = "demo"
    def __init__(self,fullname):#constructor

        self.name = fullname

        print("Student object created")

    def welcome(self):
        print("Welcome to this class")


s1 = Student("Yuvraj")
s1.welcome()


s2 = Student("Yash")
print(s2.name)

