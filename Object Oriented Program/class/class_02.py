class Student:
    def __init__(self, name,marks):
        self.name = name
        self.marks = marks
    # def hello():
    #     print("hello") error show
    def get_avg(self):
        sum = 0
        for mark in self.marks:
            sum += mark
        print(sum)



s1 = Student("James",[97,23,44])
# print(s1.name)
# print(s1.marks)
s1.get_avg()
# s1.hello()



# @staticmethod # static method also call decorator,m