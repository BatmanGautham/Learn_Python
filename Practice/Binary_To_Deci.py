

bnum = input("Enter a binary number: ")
L = len(bnum)
dnum = 0
for i in range(L-1,-1,-1):
    if bnum[i] == '1':
        dnum += 2**(i) 

print("\nDecimal equivalent : ",dnum)


bnum = input("\nEnter another binary number: ")
dnum = int(bnum, 2)
print("\nDecimal equivalent:", dnum)