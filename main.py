from tkinter import Tk
from Pengine import *

from Pengine.Modules.Rendering import Window as windowManager

from Pengine.Modules.Utilities import Utils as utils

from Pengine.Modules.Managers.ui_manager import UIElement as ui_elms

from Pengine.Modules.Utilities.premade_win import engine_info, mem_debug_info

from Pengine.Modules.Rendering import Renderer as render

import Pengine.Modules.Managers.sound_manager as sm

import platform


class callbacks:

    def test_callback():
        ei = engine_info()
       # ei.show()


mainWindow = windowManager.__create__("Pengine -- Test", 400, 750)

windowManager.set_bg_color(mainWindow, "#303030")

ui_elms.Button("Show Engine Information Window", callbacks.test_callback(),
               "#303030", "black", 0, 30, 210, mainWindow)

my_object = create_object(name="Hello",
                          object_type="text",
                          size="250x100",
                          position="0,1",
                          color="green")

mem_win = mem_debug_info()

mem_win.show()

sm.replit_play_sound("Pengine/Audio/Glasshouse.wav", 2)

store_object(my_object)

render.file_render("test_obj", mainWindow)

input()
