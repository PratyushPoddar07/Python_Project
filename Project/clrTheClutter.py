"""Write a program to clear the cutter insde a folder on you computer.
You should use os module to rename all the png images from 1.png all the way till n.png where n is the number of png files in that folder. Do the same for other file formats."""

import os

files = os.listdir("sample")
i=1
for file in files:
    if file.endswith(".png"):
        os.rename(f"sample/{file}",f"sample/{i}.png")
        print(file)
        i=i+1
