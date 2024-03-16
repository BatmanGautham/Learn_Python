m1=[]

for i in range(3):
    m1.append([])
    for j in range(3):
        a=int(input("enter the no."))
        m1[i].append(a)
mt=[]

for i in range(3):
    mt.append([])
    for j in range(3):
        t=m1[j][i]
        mt[i].append(t)


print("matrix is",m1)
print("transpose matrix is",mt)