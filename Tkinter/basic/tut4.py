from tkinter import *

root = Tk()
root.geometry("444x233")
root.title("My GUI with Harry")


# Important label option
""" 
text - adds the Text
bd - background
fg -foreground
font -set the font
font=("comicsansms",19,"bold")
padx -x padding 
pady -x padding
relief - border styling - SUNKEN, RAISED, GROOVE , RIDGE

"""

title_label = Label(text='''
Anime (Japanese: アニメ, IPA: [aꜜɲime] ⓘ) is hand-drawn \nand computer-generated animation originating from Japan. \nOutside Japan and in English, anime refers specifically to \nanimation produced in Japan.[1] However, in Japan and \nJapanese, anime (a term derived from a shortening of the \nEnglish word animation) describes all animated works, \nregardless of style or origin. Many works of animation \nwith a similar style to Japanese animation are also \nproduced outside Japan. Video games sometimes also feature \nthemes and art styles that are sometimes labelled as anime.
\n
''',bg="Green",padx=23,pady=23,font="comicsansms 19 bold",borderwidth=3,relief=SUNKEN)

# IMPORTANT PACK OPTIONS 
# anchor =n,nw,ne,e,w,s,sw,se
# side = top,bottom,left,right
# fill = x,y
# padx
# pady

title_label.pack(side=BOTTOM,anchor="s",fill=X)
root.mainloop()