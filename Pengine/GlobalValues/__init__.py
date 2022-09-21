import platform

def get_system():
    system = platform.uname()[0]
    if system == "Linux":
        from os import environ
        if "REPL_OWNER" in environ:
            return "REPLIT"
        else:
            return "LINUX"
objects = []

#object types
label = "Label"
button = "Button"
frame = "Frame"