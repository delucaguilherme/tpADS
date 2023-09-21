from tkinter import *
from .RemoveUser import *

class AdmScreen:
    def __init__(self):
        root = Tk()
        root.title('GlicMed')
        root.geometry('800x600')
        root.configure(bg="#fff")
        root.resizable(False, False)

        userBttn = Button(root, text='Excluir Usuário', bg='#57a1f8', fg='white', border=0, font=('Segoe UI', 13, 'bold'), command=lambda: [root.destroy(), self.removeUser(root)])
        userBttn.place(x = 250, y=100, width=300, height=60)

    def removeUser(self, root):
        RemoveUser(root)