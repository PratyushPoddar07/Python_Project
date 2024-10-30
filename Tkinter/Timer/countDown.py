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

# timer
hrs = StringVar()
entry = Entry(root,textvariable=hrs,width=2,font="arial 50",bg="#000",fg="#fff",bd=0)
entry.place(x=30,y=155)
hrs.set("00")

min = StringVar()
entry = Entry(root,textvariable=min,width=2,font="arial 50",bg="#000",fg="#fff",bd=0)
entry.place(x=150,y=155)
min.set("00")

sec= StringVar()
entry  = Entry(root,textvariable=sec,width=2,font="arial 50",bg="#000",fg="#fff",bd=0)
entry.place(x=270,y=155)
sec.set("00")

lab2 = Label(root,text="hours",font="arial 12",bg="#000",fg="#fff")
lab2.place(x=105,y=200)

lab2 = Label(root,text="min",font="arial 12",bg="#000",fg="#fff")
lab2.place(x=225,y=200)

lab2 = Label(root,text="sec",font="arial 12",bg="#000",fg="#fff")
lab2.place(x=345,y=200)


def Timer():
    times=int(hrs.get())*3600 + int(min.get())*60+int(sec.get())

    while times > -1:
        minute,second=(times//60,times % 60)

        hour = 0
        if minute>60:
            hour,minute=(minute//60,minute%60)

        sec.set(second)
        min.set(minute)
        hrs.set(hour)

        root.update()
        time.sleep(1)

        if (times == 0):
            playsound(r"C:\Users\shuva\Desktop\Python_Project\Tkinter\Timer\amongus.mp3")
            sec.set("00")
            min.set("00")
            hrs.set("00")

        times -= 1
def brush():
    hrs.set("00")
    min.set("02")
    sec.set("00")
    

def face():
    hrs.set("00")
    min.set("15")
    sec.set("00")

def eggs():
    hrs.set("00")
    min.set("10")
    sec.set("00")

button =Button(root,text="Start",bg="#ea3548",bd=0,fg="#fff",height=2,width=20,font="arial 10 bold",command=Timer)
button.pack(padx=5,pady=40,side=BOTTOM)


img1 = PhotoImage(file=r"C:\Users\shuva\Desktop\Python_Project\Tkinter\Timer\brush.png")
button1 = Button(root,image=img1,bg="#000",bd =0,command=brush)
button1.place(x=7,y=300)

img2 = PhotoImage(file=r"C:\Users\shuva\Desktop\Python_Project\Tkinter\Timer\face.png")
button2 = Button(root,image=img2,bg="#000",bd =0,command=face)
button2.place(x=137,y=300)

img3 = PhotoImage(file=r"C:\Users\shuva\Desktop\Python_Project\Tkinter\Timer\eggs.png")
button3 = Button(root,image=img3,bg="#000",bd =0,command=eggs)
button3.place(x=267,y=300)

root.mainloop()