from tkinter import *
import speedtest
import threading
from tkinter import ttk

def speedCheck():
    sp = speedtest.Speedtest()
    sp.get_servers()

    # Update button text to indicate that the test is running
    button.config(text="Testing...", state=DISABLED)

    # Run the test in a separate thread to avoid freezing the UI
    def run_speedtest():
        down = str(round(sp.download() / (10 ** 6), 3)) + " Mbps"
        up = str(round(sp.upload() / (10 ** 6), 3)) + " Mbps"
        lab_down.config(text=down)
        lab_up.config(text=up)
        button.config(text="Check Speed", state=NORMAL)  # Reset button after test

    threading.Thread(target=run_speedtest).start()

# Create the main window
sp = Tk()
sp.title("Internet Speed Tester")
sp.geometry("500x700")
sp.config(bg="#7AB2D3")

# Create a style for modern UI appearance
style = ttk.Style()
style.configure("TButton", font=("Arial Rounded MT Bold", 16), padding=10, borderwidth=0, relief="flat", background="#FF6363", foreground="white")

# Labels and other UI components
lab_title = Label(sp, text="Internet Speed Test", font=("Arial Rounded MT Bold", 30, "bold"), bg="#DE8F5F", fg="white")
lab_title.place(x=40, y=40, height=60, width=420)

lab_down_title = Label(sp, text="Download Speed", font=("Arial Rounded MT Bold", 22, "bold"), bg="#DE8F5F", fg="#3B1E54")
lab_down_title.place(x=40, y=130, height=50, width=420)

lab_down = Label(sp, text="00 Mbps", font=("Arial Rounded MT Bold", 22), bg="#FFFFFF", fg="#3B1E54", relief=RAISED, bd=5)
lab_down.place(x=40, y=190, height=50, width=420)

lab_up_title = Label(sp, text="Upload Speed", font=("Arial Rounded MT Bold", 22, "bold"), bg="#DE8F5F", fg="#3B1E54")
lab_up_title.place(x=40, y=280, height=50, width=420)

lab_up = Label(sp, text="00 Mbps", font=("Arial Rounded MT Bold", 22), bg="#FFFFFF", fg="#3B1E54", relief=RAISED, bd=5)
lab_up.place(x=40, y=340, height=50, width=420)

# Progress Bar to show activity
progress = ttk.Progressbar(sp, orient=HORIZONTAL, length=300, mode='indeterminate')
progress.place(x=100, y=420, height=30, width=300)

def start_progress():
    progress.start()

def stop_progress():
    progress.stop()

def run_speed_test_with_progress():
    start_progress()
    speedCheck()
    stop_progress()

# Check Speed Button
button = Button(sp, text="Check Speed", font=("Arial Rounded MT Bold", 22, "bold"), bg="#FF6363", fg="white", command=lambda: run_speed_test_with_progress())
button.place(x=40, y=500, height=60, width=420)

sp.mainloop()
