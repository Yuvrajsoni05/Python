class Person:
    name = "Deva"
    #
    # def change_name(self,name):
    #     # self.name = name
    #     # print(self.name)
    #     Person.name = name
    @classmethod
    def change_name(cls, name):
        # self.name = name
        # print(self.name)
        cls.name = name
person = Person()
person.change_name("De")
print(Person.name)
print(person.name)