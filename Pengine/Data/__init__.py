import json
from Pengine.GlobalValues import *

def store_object(data):
    global objects
    globals()["objects"].append(data)
    with open("Pengine/Data/objects.json", "w") as write_file:
        json.dump(objects, write_file)