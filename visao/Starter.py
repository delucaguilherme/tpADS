from tkinter import *
from .HomeScreen import *

class Starter:
    def __init__(self):
        root = Tk()
        root.title('GlicMed')
        root.geometry('800x600')
        root.configure(bg="#fff")
        root.resizable(False, False)

        HomeScreen(root)

        root.mainloop()
