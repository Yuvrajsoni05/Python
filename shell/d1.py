class Person():
    def set_details(self):
        self.name = 'jhon'
        self.age = '20'
        
    def display(self):
        print('i am a person',self)
    def greet(self):
        print("Hello how are you doing",self)
        
p1 = Person()
p2 = Person()

p2.set_details()

p1.display()
p2.greet()
