alphabets = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

n = int(input("Enter number of rows(1 to 26) : "))

if 1 <= n <= 26:
  for i in range(n):
    for j in range(i + 1):
        print(alphabets[j], end="")
    print()
else:
    print("\nEnter a valid number!")