from tkinter import *
import speedtest


def speedCheck():
     sp= speedtest.Speedtest()
     sp.get_servers()
     down = str(round(sp.download()/(10**6),3))+" Mbps"
     up = str(round(sp.upload()/(10**6),3))+" Mbps"
     lab_down.config(text=down)
     lab_up.config(text=up)

     




sp = Tk()
sp.title("Internet Speed Tester ")
sp.geometry("500x700")
sp.config(bg="#7AB2D3")

# label
lab = Label(sp,text="Internet Speed Test",font=("Time New Roman",33,"bold"),bg="#DE8F5F",fg="#3B1E54")
lab.place(x=40,y=40,height=50,width=420)



lab = Label(sp,text="Download Speed Test",font=("Time New Roman",33,"bold"),bg="#DE8F5F",fg="#3B1E54")
lab.place(x=40,y=130,height=50,width=420)

lab_down = Label(sp,text="00",font=("Time New Roman",33,"bold"),bg="#DE8F5F",fg="#3B1E54")
lab_down.place(x=40,y=200,height=50,width=420)

lab = Label(sp,text="Upload Speed ",font=("Time New Roman",33,"bold"),bg="#DE8F5F",fg="#3B1E54")
lab.place(x=40,y=290,height=50,width=420)

lab_up = Label(sp,text="00",font=("Time New Roman",33,"bold"),bg="#DE8F5F",fg="#3B1E54")
lab_up.place(x=40,y=360,height=50,width=420)

button= Button(sp,text="Check Speed",font=("Time New Roman",33,"bold"),bg="Red",fg="#3B1E54",relief=RAISED,command=speedCheck)
# button =Button(sp,text="Check Speed",font=("Time new Roman",30,"Bold"),relief=RAISED)
button.place(x=40,y=460,height=50,width=420)


sp.mainloop()