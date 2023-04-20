# main.py
from libs import app
import os

if __name__ == '__main__':
    if os.name == "nt":
        import ctypes
        ctypes.windll.shcore.SetProcessDpiAwareness(1)
    app = app.App()
    app.run()


