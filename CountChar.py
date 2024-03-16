str = input("Enter the string : ")

dict = {}

for i in str:
    count = 0
    for j in str:
        if i == j:
            count += 1
    dict[i] = count

print(dict)
