n = int(input("Enter the number : "))
sum = 1
for i in range(1,n+1):
    sum *= i
print("Factorial of ",n," is : ",sum)



def fact(num):
    if num == 1 or num <= 0:
        return 1
    else:
        return num*fact(num-1)

num = int(input("Enter the number : "))
print("Factorial of ",num," is : ",fact(num)) 


 
