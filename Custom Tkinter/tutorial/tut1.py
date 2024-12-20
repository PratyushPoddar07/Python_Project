from tkinter import *
import customtkinter


# Set the them and color 
customtkinter.set_appearance_mode("dark") #Modes: system(default) ,light ,dark
customtkinter.set_default_color_theme("green") #THeme : blue(default),dark-blue,green ->>>> button background



# root =Tk()
root = customtkinter.CTk() # same work as tk() -> create CTK WINDOW LIKE WE DO WITH TK()


root.title('Tkinter.com -  Custom Tkinter!')
# root.iconbitmap('images/codemy.io')  #-> icon
root.geometry('600x350')


# function
def hello():
    lab.configure(text=my_button.cget("text"))


# button
my_button = customtkinter.CTkButton(root,
        text="Hello World!!",
        command=hello,
        height=100,
        width=200
        )
my_button.pack(pady =80)

# label
lab = customtkinter.CTkLabel(root,text="")
lab.pack(pady=80)


root.mainloop()