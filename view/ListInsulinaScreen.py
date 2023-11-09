from customtkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox as tkmessagebox
from persistance.InsulinPersistance import InsulinPersistance

class ListInsulinaScreen:
    def __init__(self, email):
        
        #configuração da janela
        self.root = CTk()
        self.root.title("Listar Índice Glicêmico")
        self.root.geometry("800x600")
        self.root.resizable(False, False)
        set_appearance_mode("light")

        # Obtém dados do usuário
        result = InsulinPersistance.selectAll(email)

        self.frame_direita = CTkFrame(master=self.root, width=780, height=800)  # LightBlue
        self.frame_direita.grid(row=0, column=1, sticky="nswe")

        # Define colunas para a tabela
        colunas = ('id', 'quantity', 'type', 'date', 'time', 'meal_type', 'meal_time', 'usuario', '')

        # Cria um widget Treeview para exibir dados
        self.tabela = ttk.Treeview(self.frame_direita, columns=colunas, height=17, selectmode='browse', show='headings')

        # Configura larguras e cabeçalhos das colunas
        self.tabela.column("#1", anchor="w", minwidth=50, width=100)
        self.tabela.column("#2", anchor="w", minwidth=50, width=100)
        self.tabela.column("#3", anchor="c", minwidth=50, width=100)
        self.tabela.column("#4", anchor="c", minwidth=50, width=100)
        self.tabela.column("#5", anchor="c", minwidth=50, width=100)
        self.tabela.column("#6", anchor="c", minwidth=50, width=100)
        self.tabela.column("#7", anchor="c", minwidth=50, width=100)
        self.tabela.column("#8", anchor="c", minwidth=50, width=100)
        self.tabela.column("#9", anchor="w", minwidth=50, width=100)

        self.tabela.heading('id', text='ID')
        self.tabela.heading('quantity', text='Quantidade')
        self.tabela.heading('type', text='Tipo Insulina')
        self.tabela.heading('date', text='Data')
        self.tabela.heading('time', text='Horário')
        self.tabela.heading('meal_type', text='Refeição')
        self.tabela.heading('meal_time', text='Pré/Pós Refeição')
        self.tabela.heading('usuario', text='Usuário')
        self.tabela.heading('', text='')

        # Configura grade da tabela e barra de rolagem
        self.tabela.grid(row=0, column=0, sticky='nsew', padx=10, pady=10)
        barra_rolagem = ttk.Scrollbar(self.tabela, orient=tk.VERTICAL, command=self.tabela.yview)
        self.tabela.configure(yscroll=barra_rolagem.set)
        self.tabela.bind('<<TreeviewSelect>>', self.item_selecionado)
        self.tabela.grid(row=0, column=0, sticky=tk.NSEW)

        # Adiciona dados à tabela
        for glucose in result:
            self.tabela.insert('', tk.END, values=glucose +
                               ('EXCLUIR',), tags='button')

        self.tabela.tag_configure('button')
        self.tabela.bind('<ButtonRelease-1>', lambda event: self.confirm_delete())

        self.root.mainloop()

    # Função de retorno de chamada para seleção de item
    def item_selecionado(self, event):
        for item_selecionado in self.tabela.selection():
            item = self.tabela.item(item_selecionado)
            registro = item['values']
        self.root.mainloop()

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
                glucose_to_delete = item['values'][0]

                # Confirmação de exclusão com o usuário
                confirm = tkmessagebox.askyesno('Confirmar Exclusão', f'Tem certeza que deseja excluir o usuário {glucose_to_delete}?')

                if confirm:
                    # Remove a linha da tabela
                    self.tabela.delete(item_id)

                    result = InsulinPersistance.deleteInsulin(glucose_to_delete)

                    # Mostra a mensagem de resultado
                    tkmessagebox.showinfo('Resultado', result)
        else:
            # Nenhum item selecionado, mostra uma mensagem ou faz algo apropriado
            tkmessagebox.showinfo('Nenhum item selecionado', 'Selecione um usuário para exclusão.')