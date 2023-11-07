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

        self.email = ctk.CTkEntry(master=self.root,
                                  width=210,
                                  height=26,
                                  placeholder_text='E-mail',
                                  corner_radius=9)
        self.email.place(relx=0.5, rely=0.4, anchor=ctk.CENTER)

        searchBttn = ctk.CTkButton(self.root,
                                   text='Buscar',
                                   font=('Segoe UI', 16),
                                   width=210, height=60,
                                   command=lambda: [AdmScreen.removeUser(self)])
        searchBttn.place(relx=0.5, rely=0.63, anchor=ctk.CENTER)

    def removeUser(self):
        
        user = Usuarios()
        result = user.selectAll()
        print(result)
        total_rows = len(result)

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

        self.add_menu_display211 = ctk.CTkFrame(master=self.frame_right,
                                                corner_radius=15,
                                                height=400,
                                                width=540)
        self.add_menu_display211.grid(pady=15, padx=15, sticky="nws")

        columns = ('email', 'senha', 'tipo')

        self.table = ttk.Treeview(self.add_menu_display211, columns=columns, height=17,
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
        scrollbar = ttk.Scrollbar(self.table, orient=tk.VERTICAL, command=self.table.yview)
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