import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

# Initialize the root window
root = tk.Tk()
root.title("Daily News Bulletin")
root.geometry("800x600")

# Setting the font styles
title_font = ("Helvetica", 24, "bold")
headline_font = ("Helvetica", 18, "bold")
text_font = ("Helvetica", 12)

# Newspaper title
title_label = tk.Label(root, text="The Daily Times", font=title_font, fg="darkblue")
title_label.pack(pady=10)

# Featured article frame
feature_frame = ttk.Frame(root)
feature_frame.pack(pady=20, padx=20, fill='x')

headline_label = tk.Label(feature_frame, text="Featured Headline: Major Event Shakes the World", font=headline_font)
headline_label.grid(row=0, column=0, sticky="w", padx=10)

# Placeholder for the featured image
try:
    # Load an image (ensure the image path is correct)
    image = Image.open("path/to/your/image.jpg")
    image = image.resize((200, 200), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(image)
    image_label = tk.Label(feature_frame, image=img)
    image_label.grid(row=1, column=0, pady=10, padx=10)
except:
    image_label = tk.Label(feature_frame, text="Image Not Available", font=text_font)
    image_label.grid(row=1, column=0, pady=10, padx=10)

# Featured article content
content_label = tk.Label(feature_frame, text="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin euismod...", font=text_font, wraplength=500, justify="left")
content_label.grid(row=1, column=1, sticky="w", padx=10)

# Divider
separator = ttk.Separator(root, orient='horizontal')
separator.pack(fill='x', pady=20)

# Additional articles frame
articles_frame = ttk.Frame(root)
articles_frame.pack(padx=20, fill='x')

# Other headlines
headlines = [
    "Breaking: Stock Market Hits All-Time High",
    "Local Hero Saves Cat Stuck in Tree",
    "New Tech Innovations Revealed at Conference",
    "Weather Update: Heavy Rain Predicted in City"
]

for idx, headline in enumerate(headlines):
    article_label = tk.Label(articles_frame, text=headline, font=headline_font, fg="black")
    article_label.pack(anchor='w', pady=5)

# Start the Tkinter event loop
root.mainloop()
