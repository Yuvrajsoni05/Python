class Complex:
    def __init__(self,real,imag):
        self.real = real
        self.imag = imag
    def show_number(self):
        print(self.real, + self.imag)

    def __add__(self, num2):
        new_rel = self.real + num2.real
        new_imag = self.imag + num2.imag
        return Complex(new_rel,new_imag)


num1 = Complex(2,3)
print(type(num1.show_number))
num2  = Complex(3,4)
print(type(num2.show_number))
n4 = num1 + num2
n4.show_number()

