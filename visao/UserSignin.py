from tkinter import *
import customtkinter as ctk
from visao.PlaceholderEntry import PlaceholderEntry

class UserSignin:
    def __init__(self):
        root = ctk.CTk()
        root.title('GlicMed')
        root.geometry('800x600')
        root.configure(bg="#fff")
        root.resizable(False, False)

        heading = Label(root, text='Entrar', fg='#57a1f8', bg='white', font=('Segoe UI', 16, 'bold'))
        heading.place(x=250, y = 10)

        self.email = PlaceholderEntry(root, fg='black', border=1, placeholder="e-mail") 
        self.email.place(x=250, y=50, width=300, height=60)
        
        self.password = PlaceholderEntry(root, fg='black', border=1, placeholder="senha") 
        self.password.place(x=250, y=140, width=300, height=60)

        cmmnUserBttn = Button(root, text='Entrar', bg='#57a1f8', fg='white', border=0, font=('Segoe UI', 14, 'bold'), command=lambda: [root.destroy()])
        cmmnUserBttn.place(x=250, y=220, width=300, height=60)

        root.mainloop()

    def userSignin(self):
        

        print(f"{email}, {password}")
