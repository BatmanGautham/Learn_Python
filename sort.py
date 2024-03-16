n=int(input("Enter a limit:"))
l=[]
for i in range(n):
    n1=int(input("Enter a number:"))
    l.append(n1)
for i in range(n):
    for j in range(i+1,n):
        if(l[i]>=l[j]):
            t=l[i]
            l[i]=l[j]
            l[j]=t
print(l)