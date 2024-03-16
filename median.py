n=int(input("Enter a limit:"))
l=[]
for i in range(n):
    n1=int(input("Enter a number:"))
    l.append(n1)
l.sort()
if n%2!=0:
    n2=l[int((n-1)//2)]
else:
    n2=l[int(((n//2)+((n//2)+1))/2)]
print("Median:",n2)
    
        