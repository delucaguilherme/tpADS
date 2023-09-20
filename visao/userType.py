from tkinter import *
from .userMenu import *
from .adminMenu import *
import os

class UserType:
    def __init__(self, parent):
        frame = Frame(parent, width=800, height=400, bg='white')
        frame.place(x=200, y=100)

        self.icon_glicmed = PhotoImage(file=os.path.join(os.path.dirname(__file__), '../icons/GlicMed_icon.png'))
        self.text_glicmed = PhotoImage(file=os.path.join(os.path.dirname(__file__), '../icons/GlicMed_text.png'))
        
        glicmed_label = Label(frame, image=self.text_glicmed, bg='white')
        glicmed_label.place(x=180, y=10, height=70)

        glicmed_icon = Label(frame, image=self.icon_glicmed, bg='white')
        glicmed_icon.place(x=70, y=0, height=70)
        
        userBttn = Button(frame, text='Cadastrar Usuário', bg='#57a1f8', fg='white', border=0, font=('Segoe UI', 13, 'bold'), command=lambda: [frame.destroy(), self.userMenu(parent)])
        userBttn.place(x = 50, y=80, width=300, height=60)

        adminBttn = Button(frame, text='Fazer Login', bg='#57a1f8', fg='white', border=0, font=('Segoe UI', 13, 'bold'), command=lambda: [frame.destroy(), self.adminMenu(parent)])
        adminBttn.place(x=50, y=160, width=300, height=60)

    def userMenu(self, parent):
        UserMenu(parent)

    def adminMenu(self, parent):
        AdminMenu(parent)