from customtkinter import *
from control.RegisterUserController import RegisterUserController as Controller

class RegisterUserScreen:
    def __init__(self):
        
        #configuração da janela
        self.root = CTk()
        self.root.title("Cadastro de Usuário")
        self.root.geometry("800x600")
        self.root.resizable(False, False)
        set_appearance_mode("light")
        
        heading = CTkLabel(
            master=self.root, 
            text='Preencha as informações', 
            font=('Segoe UI', 26, 'bold')
        )
        heading.place(relx=0.5, rely=0.20, anchor=CENTER)

        self.email = CTkEntry(
            master=self.root, 
            placeholder_text="email", 
            width=210, height=30
        )
        self.email.place(relx=0.5, rely=0.34, anchor=CENTER)

        self.password = CTkEntry(
            master=self.root, 
            show="*", 
            placeholder_text="senha", 
            width=210, height=30
        )
        self.password.place(relx=0.5, rely=0.40, anchor=CENTER)

        self.password_confirm = CTkEntry(
            master=self.root, 
            show="*", 
            placeholder_text="confirmar senha", 
            width=210, height=30
        )
        self.password_confirm.place(relx=0.5, rely=0.46, anchor=CENTER)

        signup_bttn = CTkButton(
            master=self.root, 
            text='Cadastre-se',
            font=('Segoe UI', 16),
            width=210, height=30, 
            command=lambda: [Controller.register_user(self)]
        )
        signup_bttn.place(relx=0.5, rely=0.55, anchor=CENTER)
        
        return_bttn = CTkButton(
            master=self.root,
            text='Voltar para Login',
            font=('Segoe UI', 12),
            width=100, height=40,
            command=lambda: [self.root.destroy()]
        )
        return_bttn.place(relx=0.2, rely=0.9, anchor=CENTER)

        self.root.mainloop()

    def get_root(self):
        return self.root