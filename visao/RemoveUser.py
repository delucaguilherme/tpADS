from tkinter import *
from .PlaceholderEntry import *

class RemoveUser:
    def __init__(self):
        root = Tk()
        root.title('GlicMed')
        root.geometry('800x600')
        root.configure(bg="#fff")
        root.resizable(False, False)
    
        heading = Label(root, text='Remover Usuário', fg='#57a1f8', bg='white', font=('Segoe UI', 16, 'bold'))
        heading.place(x=250, y = 10)

        userID = PlaceholderEntry(root, fg='black', border=1, placeholder="ID do Usuário") 
        userID.place(x=250, y=50, width=300, height=60)

        removeBttn = Button(root, text='Remover', bg='#57a1f8', fg='white', border=0, font=('Segoe UI', 14, 'bold'), command=lambda: [self.userRemove(root), root.destroy()])
        removeBttn.place(x = 250, y=120, width=300, height=60)

    def userRemove(self):
        userID = userID.get()
        print("done")