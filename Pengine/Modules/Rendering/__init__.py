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
        objects

    # renders only with file. best if oyu know the obj is in a file
    def file_render(object_name, win_name):
        with open("Pengine/Data/objects.json") as jsonFile:
            data = jsonFile.read()
            jsonFile.close()

        data_list = data.replace('\n', ' ').split("!#@")

        
        for i in data_list:
            print(i)

    # automatically determines mem or file. slower, best if you dk where the object is
    def render():
        print('double render')
