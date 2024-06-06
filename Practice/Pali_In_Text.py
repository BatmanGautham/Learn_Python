def palindrome(str):
    new_str = str.lower()
    return new_str == new_str[::-1]

text = input("Enter your text message : ")
new_text = text.split()

pali=[]
for i in new_text:
    flag = palindrome(i)

    if flag == True:
        pali.append(i)

print("Palindrome words in given text message are : ",pali)