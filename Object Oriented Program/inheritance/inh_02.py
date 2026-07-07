class A:
    varA = "A"
class B:
    varB = "B"
class C(A,B):
    varC = "C"


c1 = C()
print(c1.varA)
print(c1.varB)

#super method
