# from tkinter import *

# root = Tk()
# root.geometry("4160x3119")

# photo = PhotoImage(file="1.png")

# lab =Label(root,image=photo)
# lab.pack()

# root.mainloop()



from tkinter import *
from PIL import Image, ImageTk  # Pillow library -> to convet jp to png

root = Tk()
root.geometry("1005x904")

# Load and convert the image with PIL
image = Image.open("2.jpg")
photo = ImageTk.PhotoImage(image)

# Display the image in a Label
lab = Label(root, image=photo)
lab.pack()

root.mainloop()
