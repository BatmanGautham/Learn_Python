str1=input("enter the sentence: ").lower()
digit=0
vowel=0
conso=0
for i in str1:
    if i.isnumeric():
        digit=digit+1
    elif i.isalpha():
        if i=='a'or i=='e'or i=='o'or i=='i'or i=='u':
            vowel=vowel+1
        else:
            conso=conso+1
    
print(digit,"\n",vowel,"\n",conso)
            
            