from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Image Viewer")

image = Image.open("colorful flowers.jpg")

# Convert the Image object into a Tkinter-compatible photo image
photo = ImageTk.PhotoImage(image)

# Create a Label widget to display the image
label = Label(root, image=photo)
label.pack()

# Start the Tkinter event loop
root.mainloop()