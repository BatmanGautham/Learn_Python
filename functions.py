def evenodd(n):
    if n%2==0:
        print("EVEN")
    else:
        print("ODD")
    
def factors(n):
    for i in range (1,n+1):
        if n%i==0:
            print(i,end="")

def posneg(n):
    if n>0:
        print("POSITIVE")
    elif n<0:
        print("NEGATIVE")
    else:
        print("ZERO")

while True:
    print("1.Even or odd\n2.Positive,negative or zero\n3.Factor\n4.Exit")
    ch=int(input("Enter your choice"))
    n=int(input("Enter a number"))

    if ch==1:
        evenodd(n)
    if ch==2:
        posneg(n)
    if ch==3:
        factors(n)
    if ch==4:
        break


