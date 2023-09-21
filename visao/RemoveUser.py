from tkinter import *
from .PlaceholderEntry import *

class RemoveUser:
    def __init__(self, parent=None):
        frame = Frame(parent, width=400, height=400, bg='red')
        frame.place(x=200, y=100)

        heading = Label(frame, text='Remover Usuário', fg='#57a1f8', bg='white', font=('Segoe UI', 16, 'bold'))
        heading.place(x=50, y = 10)

        userID = PlaceholderEntry(frame, fg='black', border=1, placeholder="ID do Usuário") 
        userID.place(x=50, y=50, width=300, height=60)

        removeBttn = Button(frame, text='Remover', bg='#57a1f8', fg='white', border=0, font=('Segoe UI', 14, 'bold'), command=lambda: [self.userRemove(parent, userID.get()), frame.destroy()])
        removeBttn.place(x = 50, y=120, width=300, height=60)

    def userRemove(self, parent, userID):
        print("done")