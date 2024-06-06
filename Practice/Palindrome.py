str = input("Enter your word : ")

new_str = str.lower()

if new_str == new_str[::-1]:
    print("Its Palindrome")
else :
    print("Not Palindrome")