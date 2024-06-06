import math as m

def fact(num):
    if num <= 1:
        return 1
    else:
        return num * fact(num - 1)
    

angD = int(input("Enter angle in degree : "))
angR = angD*(m.pi/180)

n = int(input("Enter number of terms : "))
result = 0
for i in range(n):
    sign = -1**i

    terms = (angR**(2*i))/fact(2*i)

    result += sign + terms