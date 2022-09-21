from Pengine.GlobalValues import *

def create_object(name, object_type, position, size, color):
    data = {
        name : {
            "object_type" : object_type,
            "position" : position,
            "size" : size,
            "color" : color,
        }
    }

    return data