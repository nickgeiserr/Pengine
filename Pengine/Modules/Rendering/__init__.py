import tkinter as tk
from Pengine.GlobalValues import *
import json

# Class Containing all window functionality
class Window:

    def __create__(name, _height, _width):

        
        ### window stored global ###
        window = tk.Tk()

        ### initialize win ###
        window.title(name)
        window.configure(width=_width, height=_height)
        window.configure(bg="gray")

        return window

    def destroy(window_obj):
        window_obj.destroy()

    def hide(window_obj):
        window_obj.withdraw()

    def show(window_obj):
        window_obj.deiconify()

    def set_bg_color(window_obj, color):
        window_obj.configure(bg=color)


class Renderer:

    # renders only with memory. best if you know the obj is in memory
    def mem_render(object_name, win_obj):
        for i in objects:
            object = i.get(object_name)
            if object != None:
                 break

        #object perameters
        object_type = object.get("object_type")
        object_position = object.get("position")
        object_size = object.get("size")
        object_color = object.get("color")

        #display object code here