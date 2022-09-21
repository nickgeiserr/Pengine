import os

name = "PenginePlusPlus"

os.system("g++ -shared -c -fPIC "+name+"/main.cpp -o function.o")
os.system("g++ -shared -Wl,-soname,library.so -o library.so function.o")

import ctypes
cfn=ctypes.CDLL('./library.so')

def e(x):
    cfn.hello_world(x)