import tkinter as tk
from tkinter import messagebox as tkmessagebox
from tkinter import ttk
from customtkinter import *
from CTkTable import *
from tkinter.messagebox import showinfo

from persistance.UserPersistance import UserPersistance
from control.AdminScreenController import AdminScreenController as Controller

# Configura o modo de aparência e o tema de cor padrão
set_appearance_mode("light")  # Modos: system (padrão), light, dark
set_default_color_theme("blue")  # Temas: blue (padrão), dark-blue, green


class AdminScreen:
    def __init__(self, email):
        # Inicializa a janela principal
        self.root = CTk()
        self.root.deiconify()
        self.root.title(f'Menu Administitrador - {email}')
        self.root.geometry('910x800')
        self.root.resizable(False, False)

        # Obtém dados do usuário
        result = UserPersistance.selectAll(self)

        # Define o layout da tela de administração
        self.frame_esquerda = CTkFrame(
            master=self.root, width=200, height=800)  # LightSkyBlue
        self.frame_esquerda.grid(row=0, column=0, sticky="nswe")

        self.frame_direita = CTkFrame(
            master=self.root, corner_radius=15)  # LightBlue
        self.frame_direita.grid(
            row=0, column=1, sticky="nswe", padx=15, pady=15)

        # Configura as linhas para melhor espaçamento
        self.frame_esquerda.grid_rowconfigure(0, minsize=10)
        self.frame_esquerda.grid_rowconfigure(8, minsize=20)
        self.frame_esquerda.grid_rowconfigure(11, minsize=10)

        # Cria um rótulo para o menu
        self.menu = CTkLabel(self.root, text=f'MENU', text_color='#57a1f8', font=(
            'Segoe UI', 20, 'bold'), bg_color='transparent')
        self.menu.place(relx=0.13, rely=0.05, anchor=CENTER)

        botao_adm = CTkButton(self.root, text='Cadastrar Adm', font=(
            'Segoe UI', 16), width=140, height=50, command=lambda: [Controller.open_register_admin_screen()])
        botao_adm.place(relx=0.13, rely=0.5, anchor=CENTER)

        botao_sair = CTkButton(self.root,
                               text='Sair',
                               font=('Segoe UI', 16),
                               width=80,
                               height=40,
                               command=lambda: [self.root.destroy()])
        botao_sair.place(relx=0.13, rely=0.9, anchor=CENTER)

        # Define colunas para a tabela
        colunas = ('email', 'senha', 'tipo', '')

        # Cria um widget Treeview para exibir dados
        self.tabela = ttk.Treeview(
            self.frame_direita, columns=colunas, height=17, selectmode='browse', show='headings')

        # Configura larguras e cabeçalhos das colunas
        self.tabela.column("#1", anchor="w", minwidth=100, width=200)
        self.tabela.column("#2", anchor="w", minwidth=100, width=200)
        self.tabela.column("#3", anchor="c", minwidth=120, width=130)
        self.tabela.column("#4", anchor="c", minwidth=120, width=130)

        self.tabela.heading('email', text='E-mail')
        self.tabela.heading('senha', text='Senha')
        self.tabela.heading('tipo', text='Tipo')
        self.tabela.heading('', text='')

        # Configura grade da tabela e barra de rolagem
        self.tabela.grid(row=0, column=0, sticky='nsew', padx=10, pady=10)
        barra_rolagem = ttk.Scrollbar(
            self.tabela, orient=tk.VERTICAL, command=self.tabela.yview)
        self.tabela.configure(yscroll=barra_rolagem.set)
        self.tabela.bind('<<TreeviewSelect>>', self.item_selecionado)
        self.tabela.grid(row=0, column=0, sticky=tk.NSEW)

        # Adiciona dados à tabela
        for usuario in result:
            self.tabela.insert('', tk.END, values=usuario +
                               ('EXCLUIR',), tags='button')

        self.tabela.tag_configure('button')
        self.tabela.bind('<ButtonRelease-1>',
                         lambda event: self.confirm_delete())

        self.root.mainloop()

    # Função de retorno de chamada para seleção de item
    def item_selecionado(self, event):
        for item_selecionado in self.tabela.selection():
            item = self.tabela.item(item_selecionado)
            registro = item['values']

    def confirm_delete(self):
        # Obtém os itens selecionados
        selected_items = self.tabela.selection()

        # Verifica se há itens selecionados
        if selected_items:
            # Obtém o primeiro item selecionado
            item_id = selected_items[0]
            item = self.tabela.item(item_id)

            # Verifica se 'values' não está vazio antes de acessar o índice
            if item['values']:
                email_to_delete = item['values'][0]

                # Confirmação de exclusão com o usuário
                confirm = tkmessagebox.askyesno(
                    'Confirmar Exclusão', f'Tem certeza que deseja excluir o usuário {email_to_delete}?')

                if confirm:
                    # Remove a linha da tabela
                    self.tabela.delete(item_id)

                    result = UserPersistance.deleteUser(email_to_delete)

                    # Mostra a mensagem de resultado
                    tkmessagebox.showinfo('Resultado', result)
        else:
            # Nenhum item selecionado, mostra uma mensagem ou faz algo apropriado
            tkmessagebox.showinfo('Nenhum item selecionado',
                                  'Selecione um usuário para exclusão.')
