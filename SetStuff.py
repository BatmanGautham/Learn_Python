print("Set operations\n")

set1 = {1,2,3}
print("Set1 is",set1)

set1.add(4)
print("\nAdded element 4 : ",set1)

set1.remove(4)
print("\nRemoved element 4 : ",set1)

if 1 in set1:
    print("1 is present in my set")
else:
    print("1 is not present")

myList = [1,2,2,2,3]
print("\nMy list is : ",myList)

print("Removing duplicates ! ")

new_list = list(set(myList))

print("New List : ",new_list)

list1 = [1,2,3,4]
list2 = [3,4,5,6]

commonList = list(set(list1).intersection(set(list2)))



