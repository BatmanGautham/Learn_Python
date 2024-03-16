str1=input("enter the sentence: ")
word=str1.split()
for element in word:
    if len(element)>5:
        print(element)