print("\nBinary to Decimal\n")

def binary(n):
    bn = ""
    while n>0 :
        val = str(n%2)
        bn = val+bn
        n = n//2
    
    return bn

num = int(input("Enter a decimal number : "))

print("Binary number is : ",binary(num))


num = int(input("Enter another decimal number: "))

binval = bin(num)[2:]

print("Binary number is : ",binval)
