import math as m

def fact(num):
    if num <= 1:
        return 1
    else:
        return num * fact(num - 1)

print("Taylor Series (Sine)")

angD = int(input("Enter angle in degrees: "))
angR = angD * (m.pi / 180)  

n = int(input("Enter number of terms: "))

result = 0
for i in range(n):
    sign = (-1) ** i  
    term = (angR ** (2 * i + 1)) / fact(2 * i + 1)
    result += sign * term

print("Sin(", angD, ") =", result)
