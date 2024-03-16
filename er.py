f=open("code.txt",'w')
f.write("programming in python")
f.close()

f=open('code.txt','r')
while True:
    line=f.readline()
    if line=="":
        break
    print(line)