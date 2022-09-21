# Windows

## Creation

Creating windows in pengine is very, very easy. It can be done by running the create function in the Window class. 

### Example :
```python
from Pengine.Modules.Rendering import Window as windowManager

windowObject = windowManager.__create__(name, height, width)
```

###  

The **windowObject** is required for rendering parts, adding UI, and a lot more. Make sure it is not lost.