mat1=[]
for i in range(3):
    mat1.append([])
    for j in range(3):
        x=int(input("Enter a number:"))
        mat1[i].append(x)
print(mat1)

mat2=[]
for i in range(3):
    mat2.append([])
    for j in range(3):
        x=int(input("Enter a number:"))
        mat2[i].append(x)
print(mat2)

mat3=[]
for i in range(3):
    mat3.append([])
    for j in range(3):
        x=mat1[i][j]+mat2[i][j]
        mat3[i].append(x)
print(mat3)


