"""Create a dictionary of names and birthdays. 
Write prog that asks the user to enter a name, 
and the program display the birthday of that person"""

d = {'Aravind':'25-02-2003', 'Fullvind':'32-13-2003'}

str = input("Enter the name of the person : ")

for i in d:
    if i == str:
        print(d[i])
        break