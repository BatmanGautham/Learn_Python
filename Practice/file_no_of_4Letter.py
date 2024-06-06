print("\nFind number of four letters")

content = input("Enter your string : ")
f = open("fourletter.txt","w")
f.write(content)
f.close()

f = open("fourletter.txt","r")
file_contents = f.read()
f.close()

content_array = file_contents.split()

words = []
count = 0
for i in content_array:
    if len(i) == 4:
        words.append(i)
        count += 1

if count == 0:
    print("No four letter words found!")
else :
    print(count," four letter words found!")
    print("They are : ",words)

