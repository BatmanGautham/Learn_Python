n = int(input("Enter number: "))
factors = []

for i in range(2, n ):
    if n % i == 0:
        flag = 0
        for j in range(2,(i//2) + 1):
            if i % j == 0:
                flag = 1
                break
        if flag == 0:
            factors.append(i)

print("Prime Factors of", n, "are:", factors)


            
