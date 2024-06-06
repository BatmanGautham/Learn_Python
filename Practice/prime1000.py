prime_num = []

for i in range(2,1000):
    flag = 0
    for j in range(2,(i//2)+1):
        if i%j == 0:
            flag = 1
            break
    if flag == 0:
        prime_num.append(i)
print("Prime numbers are : ",prime_num)