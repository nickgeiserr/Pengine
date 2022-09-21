from Pengine.Modules.Rendering import Window as windowManager

from Pengine.Modules.Utilities import Utils as utils

from Pengine.Modules.Managers.ui_manager import UIElement as ui_elms

from Pengine.Modules.Utilities import memory as mem


class engine_info:

    def test_callback(self):
        print("callback")

    def show(self):
        engineWindow = windowManager.__create__("Engine Information", 250, 500)

        windowManager.set_bg_color(engineWindow, "#303030")

        ui_elms.Text("Engine Version :", "#303030", "white", "HelveSystemtica",
                     20, 30, 30, engineWindow)
        ui_elms.Text("1.0.0", "#303030", "#ffbe8a", "System", 15, 30, 60,
                     engineWindow)

        ui_elms.Text("Developers :", "#303030", "white", "System", 20, 30, 90,
                     engineWindow)
        ui_elms.Text("Pirona Tech", "#303030", "#ff978a", "System", 15, 30,
                     120, engineWindow)

        ui_elms.Text("Current Window Name :", "#303030", "white", "System", 20,
                     30, 150, engineWindow)
        ui_elms.Text("Engine Information", "#303030", "#ffbe8a", "System", 15,
                     30, 180, engineWindow)


class mem_debug_info:

    def show(self):
        mem_debug_window = windowManager.__create__("Debug Panel", 400, 750)

        windowManager.set_bg_color(mem_debug_window, "#303030")

        ui_elms.Text("Debug Panel", "#303030", "white", "System", 30, 30, 15,
                     mem_debug_window)

        ui_elms.Text("CPU Usage", "#303030", "white", "System", 20, 30, 60,
                     mem_debug_window)
        ui_elms.Text(
            str(mem.debug_data.get_cpu_usage()) + "%", "#303030", "#4d8bff",
            "System", 20, 30, 90, mem_debug_window)

        ui_elms.Text("Resident-Set-Size", "#303030", "white", "System", 20, 30,
                     120, mem_debug_window)
        ui_elms.Text(str(mem.debug_data.get_res_set_size()), "#303030",
                     "#63996c", "System", 20, 30, 150, mem_debug_window)
