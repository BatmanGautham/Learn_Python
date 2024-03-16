str = input("Enter string : ")

myset = set(str)

dict1 = dict()

for i in myset:
    count = str.count(i)
    dict1[i] = count

print(dict1)