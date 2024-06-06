print("Count of Odd and Even numbers")

n = int(input("Enter number of numbers : "))

count = 0

for i in range(n):
    x = int(input("Enter number : "))
    if x%2 == 0:
        count += 1

print("Number of Odds :  ",n-count)
print("Number of Evens :  ",count)

