'''
d={}
for i in range(1,4):
    n=input("enter the name : ")
    d[n]=input("enter the birthday : ")
s=input("enter the name for birthday :")
print(d[s])
'''
'''
d={}
for i in range(1,5):
    d[i]=i*i
s=0
for value in d.values():
    s=s+value
print(s)
'''
'''
set1=[1,1,1,2,2,3,3,3,4]
print(list(set(set1)))
set2={3,4,5}
print(set2)
print(set1.union(set2))
'''
'''
l1=[1,2,5]
l2=[2,3,4]
print(list(set(l1).intersection(set(l2))))
'''


d={}
n=input("enter the string : ")
for i in n:
    c=0
    for j in n:
        if(i==j):
            c=c+1
    d[i]=c
print(d)
        
