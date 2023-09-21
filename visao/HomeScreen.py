from tkinter import *
from .RegisterUser import *
from .UserSignin import *
import os

class HomeScreen:
    def __init__(self, parent):
        frame = Frame(parent, width=400, height=400, bg='red')
        frame.place(x=200, y=100)

        self.icon_glicmed = PhotoImage(file=os.path.join(os.path.dirname(__file__), '../icons/GlicMed_icon.png'))
        self.text_glicmed = PhotoImage(file=os.path.join(os.path.dirname(__file__), '../icons/GlicMed_text.png'))
        
        glicmed_label = Label(frame, image=self.text_glicmed, bg='white')
        glicmed_label.place(x=180, y=10, height=70)

        glicmed_icon = Label(frame, image=self.icon_glicmed, bg='white')
        glicmed_icon.place(x=70, y=0, height=70)

        userBttn = Button(frame, text='Cadastrar Usuário', bg='#57a1f8', fg='white', border=0, font=('Segoe UI', 13, 'bold'), command=lambda: [frame.destroy(), self.registerUser(parent)])
        userBttn.place(x = 50, y=100, width=300, height=60)

        adminBttn = Button(frame, text='Fazer Login', bg='#57a1f8', fg='white', border=0, font=('Segoe UI', 13, 'bold'), command=lambda: [frame.destroy(), self.userLogin(parent)])
        adminBttn.place(x=50, y=170, width=300, height=60)

    def registerUser(self, parent):
        RegisterUser(parent)

    def userLogin(self, parent):
        UserSignin(parent)