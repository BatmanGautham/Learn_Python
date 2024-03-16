mat1=[]
for i in range(3):
    mat1.append([])
    for j in range(3):
        x=int(input("Enter a number:"))
        mat1[i].append(x)
print(mat1)

transposed=[]
for i in range(3):
    transposed.append([])
    for j in range(3):
        transposed[i].append(mat1[j][i])
print(transposed)        