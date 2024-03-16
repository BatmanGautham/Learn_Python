print("Dictionary Operations")

dict = {'Apple':2,'Orange':6}

print(dict['Apple'])

print(dict)

dict['Mango']=4

print(dict)

del dict['Mango']

print(dict)

print("\nKey values are : ")
for key in dict:
    print(key)

print("\nValues are : ")
for value in dict.values():
    print(value)
print("\nItems are :")
for key,value in dict.items():
    print(key,value)

dict2 = {1,2}
sum = 0 

for i in dict.values():
    sum =+ i

print(sum)