from tkinter import *

root = Tk()
root.title("Calculate Age")

label = Label(root, text="Enter DOB: ")
label.pack(pady=50)

day = Entry(root, width=20)
day.insert(0, "Day (xx)")  # Set default text inside the entry field
day.pack(pady=20)

month = Entry(root, width=20)
month.insert(0, "Month (xx)")
month.pack(pady=20)

year = Entry(root, width=20)
year.insert(0, "Year (xxxx)")
year.pack(pady=20)

def CalcAge():
    # Retrieve user input and remove default text
    ipDay = day.get().replace("Day (xx) : ", "")
    ipMon = month.get().replace("Month (xx) : ", "")
    ipYear = year.get().replace("Year (xxxx) : ", "")

    # Check if any of the fields are empty
    if not ipDay or not ipMon or not ipYear:
        resultLabel.config(text="Please enter all fields")
        return

    # Convert to integers
    try:
        ipDay = int(ipDay)
        ipMon = int(ipMon)
        ipYear = int(ipYear)
    except ValueError:
        resultLabel.config(text="Invalid input")
        return

    # Calculate age
    age = 2024 - ipYear

    if ipMon <= 6:
        if ipDay < 5 and ipMon == 6:
            resultLabel.config(text=age)
    else:
        age -= 1
        resultLabel.config(text=age)

button = Button(root, text="Calculate Age", command=CalcAge, fg="green")
button.pack(side=LEFT)

resultLabel = Label(root, text="")
resultLabel.pack()

root.mainloop()
