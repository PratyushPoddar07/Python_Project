from tkinter import *
from playsound import playsound

import time

root =Tk()

root.title("Asur Timer")
root.geometry("400x600")
root.config(bg="#000")
root.resizable(False,False)

heading = Label(root,text="Timer",font="arial 30 bold",bg="#000",fg="#ea3548")
heading.pack(pady=10)

# clock
lab =Label(root,font=("arial",15,"bold"),text="current time:",bg="papaya whip")
lab.place(x=65,y=70)



current_time = Label(root,font=("arial",15,"bold"),text="",fg="#000",bg="#fff")
current_time.place(x=190,y=70)

def clock():
    clock_time = time.strftime('%H:%M:%S %p')
    current_time.config(text=clock_time)
    current_time.after(1000,clock)

clock()

root.mainloop()