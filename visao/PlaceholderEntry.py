import tkinter as tk

class PlaceholderEntry(tk.Entry):
    def __init__(self, master, password = 0, placeholder=None, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.placeholder = placeholder
        self.insert(0, self.placeholder)
        self.password = password

        self.bind("<FocusIn>", self.focusIn)
        self.bind("<FocusOut>", self.focusOut)

    def focusIn(self, _):
        if self.get() == self.placeholder:
            self.delete(0, tk.END)
            if (self.password == 1):
                self.config(show="*")


    def focusOut(self, _):
        if self.get() == "":
            self.insert(0, self.placeholder)
            self.config(show="")