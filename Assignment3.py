#Task 1
def Fact(n):
    if n<2:
        return 1
    else:
        return n*(Fact(n-1))
F=Fact(5)
print(F)

#Task 2
num=int(input("Enter a number:"))
from math import *
print(f"square root of {num} is:",sqrt(num))
print("Natural log",log1p(num))
print("sine",sin(num))

