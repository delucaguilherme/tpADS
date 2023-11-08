import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from .User import Usuarios
from CTkTable import *
import tktabl
from tkinter.messagebox import showinfo

ctk.set_appearance_mode("dark")  # Modes: system (default), light, dark
ctk.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green


class AdmScreen:
    def __init__(self):
        self.root = ctk.CTk()
        self.root.deiconify()
        self.root.title('GlicMed')
        # Definindo às dimensões
        self.root.geometry('800x600')

        user = Usuarios()
        result = user.selectAll()

        # Definindo layout da tela de admin
        self.frame_left = ctk.CTkFrame(master=self.root,
                                       width=200,
                                       height=800,
                                       corner_radius=0)
        self.frame_left.grid(row=0, column=0, sticky="nswe")

        self.frame_right = ctk.CTkFrame(master=self.root)
        self.frame_right.grid(row=0, column=1, sticky="nswe", padx=15, pady=15)

        self.frame_left.grid_rowconfigure(0, minsize=10)
        self.frame_left.grid_rowconfigure(8, minsize=20)
        self.frame_left.grid_rowconfigure(11, minsize=10)

        self.frame_left = ctk.CTkFrame(master=self.frame_right,
                                       corner_radius=15,
                                       height=400,
                                       width=540)
        self.frame_left.grid(pady=15, padx=15, sticky="nws")

        self.menu = ctk.CTkLabel(self.root, text=f'MENU', text_color='#57a1f8', font=(
            'Segoe UI', 20, 'bold'), bg_color='transparent')
        self.menu.place(relx=0.13, rely=0.05, anchor=ctk.CENTER)

        userBttn = ctk.CTkButton(self.root,
                                 text='Usuários',
                                 font=('Segoe UI', 16),
                                 width=140,
                                 height=50,
                                 command=self.userScreen)
        userBttn.place(relx=0.13, rely=0.35, anchor=ctk.CENTER)

        admnBttn = ctk.CTkButton(self.root,
                                 text='Cadastrar Adm',
                                 font=('Segoe UI', 16),
                                 width=140,
                                 height=50,
                                 command=lambda: [AdmScreen.registerAdm(self)])
        admnBttn.place(relx=0.13, rely=0.5, anchor=ctk.CENTER)

        exitBttn = ctk.CTkButton(self.root,
                                 text='Sair',
                                 font=('Segoe UI', 16),
                                 width=80,
                                 height=40)

        exitBttn.place(relx=0.13, rely=0.9, anchor=ctk.CENTER)

        columns = ('email', 'senha', 'tipo')

        self.table = ttk.Treeview(self.frame_left, columns=columns, height=17,
                                  selectmode='browse',
                                  show='headings')

        self.table.column("#1", anchor="w", minwidth=100, width=200)
        self.table.column("#2", anchor="w", minwidth=100, width=200)
        self.table.column("#3", anchor="c", minwidth=120, width=130)

        # Define o cabeçalho da tabela
        self.table.heading('email', text='E-mail')
        self.table.heading('senha', text='Senha')
        self.table.heading('tipo', text='Tipo')

        self.table.grid(row=0, column=0, sticky='nsew', padx=10, pady=10)
        # add a scrollbar
        scrollbar = ttk.Scrollbar(
            self.table, orient=tk.VERTICAL, command=self.table.yview)
        self.table.configure(yscroll=scrollbar.set)
        self.table.bind('<<tableviewSelect>>', AdmScreen.item_selected)
        self.table.grid(row=0, column=0, sticky=tk.NSEW)

        # add data to the tableview
        for usuario in result:
            self.table.insert('', tk.END, values=usuario)

    def item_selected(self, event):
        for selected_item in self.table.selection():
            item = self.table.item(selected_item)
            record = item['values']
            # show a message
            showinfo(title='Information', message=','.join(record))

    def userScreen(self):
        self.heading.place_forget()
        self.email.place_forget()
        self.password.place_forget()
        self.password_confirm.place_forget()
        self.loginBttn.place_forget()
        # Exibe a tabela novamente
        self.table.grid()

    def registerAdm(self):
        self.table.grid_remove()

        self.heading = ctk.CTkLabel(
            self.root, text='Preencha as informações', text_color='#57a1f8', font=('Segoe UI', 26, 'bold'))
        self.heading.place(relx=0.6, rely=0.1, anchor=ctk.CENTER)

        self.email = ctk.CTkEntry(self.root, placeholder_text="Email")
        self.email.place(relx=0.6, rely=0.2, anchor=ctk.CENTER)

        self.password = ctk.CTkEntry(
            self.root, show="*", placeholder_text="Senha")
        self.password.place(relx=0.6, rely=0.3, anchor=ctk.CENTER)

        self.password_confirm = ctk.CTkEntry(
            self.root, show="*", placeholder_text="Confirmar Senha")
        self.password_confirm.place(relx=0.6, rely=0.4, anchor=ctk.CENTER)

        self.loginBttn = ctk.CTkButton(self.root,
                                       text='Cadastrar Usuário',
                                       font=('Segoe UI', 16),
                                       width=210, height=60,)
        self.loginBttn.place(relx=0.6, rely=0.6, anchor=ctk.CENTER)
