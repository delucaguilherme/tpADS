from customtkinter import *

class DeleteScreen:
    def __init__(self):
        
        #configuração da janela
        root = CTk()
        root.title("Excluir Usuário")
        root.geometry("800x600")
        root.resizable(False, False)
        set_appearance_mode("light")

        root.mainloop()