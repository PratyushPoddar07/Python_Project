from tkinter import *

root = Tk()

# width X height
root.geometry("733x433")
# width.height(min)
root.minsize(210,100)
# width,height(max)
root.maxsize(1200,988) 

lab = Label(text="Shuvam is a good boy")
lab.pack()

root.mainloop()