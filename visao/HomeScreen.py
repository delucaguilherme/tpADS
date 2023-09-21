from tkinter import *
from .RegisterUser import *
from .UserSignin import *
import os

class HomeScreen:
    def __init__(self):
        root = Tk()
        root.title('GlicMed')
        root.geometry('800x600')
        root.configure(bg="#fff")
        root.resizable(False, False)

        icon_glicmed = PhotoImage(file=os.path.join(os.path.dirname(__file__), '../icons/GlicMed_icon.png'))
        text_glicmed = PhotoImage(file=os.path.join(os.path.dirname(__file__), '../icons/GlicMed_text.png'))
        
        glicmed_label = Label(root, image=text_glicmed, bg='white')
        glicmed_label.place(x=380, y=10, height=70)    

        glicmed_icon = Label(root, image=icon_glicmed, bg='white')
        glicmed_icon.place(x=270, y=0, height=70)

        userBttn = Button(root, text='Cadastrar Usuário', bg='#57a1f8', fg='white', border=0, font=('Segoe UI', 13, 'bold'), command=lambda: [RegisterUser()])
        userBttn.place(x=250, y=100, width=300, height=60)

        adminBttn = Button(root, text='Fazer Login', bg='#57a1f8', fg='white', border=0, font=('Segoe UI', 13, 'bold'), command=lambda: [UserSignin()])
        adminBttn.place(x=250, y=170, width=300, height=60)

        root.mainloop()