numbers = []
for i in range(100,1000):
    temp = i
    sum = 0
    while(i > 0):
        rem = i%10
        sum += rem
        i = i//10
    if sum%9 == 0:
        numbers.append(temp)

print(numbers)