def evenodd(n):
        if(n%2==0):
            print(n," is even\n")
        else:
         print(n," is odd\n")

def posneg(n):
        if(n>0):
            print(n," is +ve\n")
        elif n<0:
            print(n,"the no. is -ve\n")
        elif n==0:
            print("The no is zero\n")           

def factors(n):
        for i in range(1,n+1):
            if n%i==0:
             print(i)  
             
while True:
    print("1.Even or Odd\n2.+ve -ve or zero\n3.Factors\n4.Excit\n")

    ch=int(input("enter your choice:\n"))
    n=int(input("enter the number:\n"))
    if ch==1:
       evenodd(n)
    if ch==2:
        posneg(n)
    if ch==3:
        factors(n)
    if ch==4:
        exit()
        break

    
        
     

                                      
        