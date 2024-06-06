def gcd(a,b):
    while b:
        a,b = b,a%b
    return a

num1 = int(input("\nEnter first num : "))
num2 = int(input("Enter second num : "))

print("\nThe Greatest Common Divisor is : ",gcd(num1,num2))