from subprocess import call
from tkinter import Label,Button
from PIL import Image, ImageTk


class UIElement:

    class Text:

        def __init__(self, s_text, bg_color, fg_color, font, fontsize, posx,
                     posy, windowObj):
            text = Label(windowObj,
                         text=s_text,
                         fg=fg_color,
                         bg=bg_color,
                         font=(font, fontsize))
            text.place(x=posx, y=posy)

    class Button:
        def __init__(self, b_text, callback, bg_color, fg_color, border, posx, posy, windowObj):
                    btn = Button(windowObj, text=b_text, bd =border,command = callback)
                    btn.place(x=posx, y=posy)

    class Image:
      def __init__(self, image_src, posx, posy, windowObj):
        img = Image.open(image_src)
        tkimgone = ImageTk.PhotoImage(img)
        
        tkimg = Label(image=tkimgone)
        tkimg.image = tkimgone
        
        windowObj.place(x=posx, y=posy)


#what the holy fuck is this spaghetti code

#the code isn't spgahetti, it's just replit's shitty formatting

#put all of your imports in __init__.py so all u have to do is import Pegine but dont loop it so stuff like global values should not be imported through the __init__ file so you dont end up with a memory loop

#basicaly if u copy and paste lines 3-7 in main.py into Pengine/__init__.py it will work the same and save some lines
