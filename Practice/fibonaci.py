n = int(input("Enter the number of terms: "))

a = 0
b = 1

if n <= 0:
    print("Please enter a positive integer!")
elif n == 1:
    print("Fibonacci Series : \n", a)
else:
    print("Fibonacci Series:")
    print(a)
    print(b)
    
    for i in range(3, n + 1):
        c = a + b
        print(c)
        a = b
        b = c
