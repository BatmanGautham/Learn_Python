import math as m
n=int(input("enter the n0: of terms:\n"))
x=int(input("enter the angle in degrees:\n"))
a=x
x=x*(m.pi/180)
sin=0
fact=1
for i in range(n):
    sign=(-1)**i
    fact=fact*(2*i+1)
    sin+=sign*(x**(2*i+1))/fact
print("sin(",a,")=",sin)    
    
    
    