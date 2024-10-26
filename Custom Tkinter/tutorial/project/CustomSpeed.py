import customtkinter as ctk
import speedtest
import threading

# Set the appearance mode and color theme
ctk.set_appearance_mode("System")  # Modes: "System", "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue", "green", "dark-blue"

def speedCheck():
    sp = speedtest.Speedtest()
    sp.get_servers()

    # Update button text to indicate that the test is running
    button.configure(text="Testing...", state="disabled")
    progress.start()  # Start progress bar

    # Run the test in a separate thread to avoid freezing the UI
    def run_speedtest():
        down = str(round(sp.download() / (10 ** 6), 3)) + " Mbps"
        up = str(round(sp.upload() / (10 ** 6), 3)) + " Mbps"
        
        # Update the labels with the download and upload speeds
        lab_down.configure(text=down)
        lab_up.configure(text=up)
        
        # Stop the progress bar and reset the button after the test
        progress.stop()
        button.configure(text="Check Speed", state="normal")  # Reset button after test

    # Start the thread to run the speed test
    threading.Thread(target=run_speedtest).start()

# Create the main window
sp = ctk.CTk()
sp.title("Internet Speed Tester")
sp.geometry("500x700")

# Labels and other UI components
lab_title = ctk.CTkLabel(sp, text="Internet Speed Test", font=("Arial Rounded MT Bold", 30), text_color="white", fg_color="#DE8F5F")
lab_title.pack(pady=(40, 10))

lab_down_title = ctk.CTkLabel(sp, text="Download Speed", font=("Arial Rounded MT Bold", 22), text_color="#3B1E54", fg_color="#DE8F5F")
lab_down_title.pack(pady=10)

lab_down = ctk.CTkLabel(sp, text="00 Mbps", font=("Arial Rounded MT Bold", 22), fg_color="#FFFFFF", text_color="#3B1E54", corner_radius=8)
lab_down.pack(pady=10)

lab_up_title = ctk.CTkLabel(sp, text="Upload Speed", font=("Arial Rounded MT Bold", 22), text_color="#3B1E54", fg_color="#DE8F5F")
lab_up_title.pack(pady=10)

lab_up = ctk.CTkLabel(sp, text="00 Mbps", font=("Arial Rounded MT Bold", 22), fg_color="#FFFFFF", text_color="#3B1E54", corner_radius=8)
lab_up.pack(pady=10)

# Progress Bar to show activity
progress = ctk.CTkProgressBar(sp, width=300)
progress.pack(pady=20)

# Check Speed Button
button = ctk.CTkButton(sp, text="Check Speed", font=("Arial Rounded MT Bold", 22), fg_color="#FF6363", text_color="white", command=speedCheck)
button.pack(pady=40)

# Run the main window loop
sp.mainloop()
