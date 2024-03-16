m1=[]
for i in range(3):
    m1.append([])
    for j in range(3):
        x=int(input("enter element"))
        m1[i].append(x)
print(m1)

m2=[]
for i in range(3):
    m2.append([])
    for j in range(3):
        y=int(input("Enter no."))
        m2[i].append(y)

print(m2)

m3=[]
for i in range(3):
    m3.append([])
    for j in range(3):
        t=m1[i][j]+m2[i][j]
        m3[i].append(t)

print("matrix 1",m1)
print("martix 2",m2)
print("sum of matrix:",m3)