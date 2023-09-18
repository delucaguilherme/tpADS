from tkinter import *
from .userType import *

class Application:
    def __init__(self):
        root = Tk()
        root.title('Diabetes')
        root.geometry('800x600')
        root.configure(bg="#fff")
        root.resizable(False, False)

        #print(font.nametofont("TkDefaultFont").actual())

        UserType(root)

        root.mainloop()
