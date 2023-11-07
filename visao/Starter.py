from tkinter import *
import customtkinter as ctk
from .HomeScreen import *

ctk.set_appearance_mode("Light")  # Modes: system (default), light, dark
ctk.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

class Starter:
    def __init__(self):
        root = ctk.CTk()
        root.title('GlicMed')
        root.geometry('800x600')
        root.configure(bg="#fff")
        root.resizable(False, False)

        HomeScreen(root)

        root.mainloop()
