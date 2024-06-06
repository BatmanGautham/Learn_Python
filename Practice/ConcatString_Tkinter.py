from tkinter import *

root = Tk()
root.title("Concatenate Your Strings!")

label1 = Label(root, text="Enter First String :")
label1.pack(pady=50,side=LEFT)

first_ip = Entry(root, width=20)
first_ip.pack(side=LEFT)

label2 = Label(root, text="Enter Second string :")
label2.pack(pady=50,side=RIGHT)

second_ip = Entry(root, width=20)
second_ip.pack(side=RIGHT)

def concat():
    resultLabel.config(text=first_ip.get() + second_ip.get())

concatB = Button(root, text="Concatenate", command=concat, fg = "green")
concatB.pack()

resultLabel = Label(root, text="")
resultLabel.pack(side=BOTTOM,pady=80)

root.mainloop()
