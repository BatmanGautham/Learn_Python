print("\nWrite and read from file")
file_text = input("\nEnter the text to write : ")

f = open("sample1.txt","w")
f.write(file_text)
f.close()

f = open("sample1.txt","r")
file_contents = f.read()
f.close()
print("Reading the file contents : ", file_contents)