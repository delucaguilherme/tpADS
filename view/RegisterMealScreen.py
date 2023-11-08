from customtkinter import *
from tkcalendar import *
from tktimepicker import *
from control.RegisterUserController import RegisterUserController as Controller

class RegisterMealScreen:
    def __init__(self):
        
        #configuração da janela
        self.root = CTk()
        self.root.title("Registrar Refeição")
        self.root.geometry("800x600")
        self.root.resizable(False, False)
        set_appearance_mode("light")

        radio_var = StringVar(value="default")
        
        heading = CTkLabel(
            master=self.root, 
            text='Preencha as informações', 
            font=('Segoe UI', 26, 'bold')
        )
        heading.place(relx=0.5, rely=0.20, anchor=CENTER)

        self.sugar_level = CTkEntry(
            master=self.root, 
            placeholder_text="carboidratos (g)", 
            width=210, height=30
        )
        self.sugar_level.place(relx=0.5, rely=0.34, anchor=CENTER)

        self.date = CTkEntry(
            master=self.root, 
            placeholder_text="data", 
            width=210, height=30
        )
        self.date.place(relx=0.5, rely=0.40, anchor=CENTER)
        self.date.bind("<1>", self.pick_date)

        self.time = CTkEntry(
            master=self.root, 
            placeholder_text="horário", 
            width=210, height=30
        )
        self.time.place(relx=0.5, rely=0.46, anchor=CENTER)
        self.time.bind("<1>", self.pick_time)

        self.meal_type = CTkComboBox(
            master=self.root, 
            values=["Café da Manhã", "Almoço", "Café da Tarde", "Janta"]
        )
        self.meal_type.place(relx=0.5, rely=0.52, anchor=CENTER)

        signup_bttn = CTkButton(
            master=self.root, 
            text='Registrar Refeição',
            font=('Segoe UI', 16),
            width=210, height=30, 
            command=lambda: [self.root.destroy()]
        )
        signup_bttn.place(relx=0.5, rely=0.67, anchor=CENTER)
        
        return_bttn = CTkButton(
            master=self.root,
            text='Voltar para Menu do Usuário',
            font=('Segoe UI', 12),
            width=100, height=40,
            command=lambda: [self.root.destroy()]
        )
        return_bttn.place(relx=0.2, rely=0.9, anchor=CENTER)

        self.root.mainloop()

    def get_root(self):
        return self.root
    
    def pick_date(self, event):
        global cal, date_window
        
        date_window = CTkToplevel()
        date_window.grab_set()
        date_window.title('Escolha a data da aplicação')
        date_window.geometry('250x220')
        cal = Calendar(date_window, selectmode="day", date_pattern="dd/mm/y")
        cal.place(x=0, y=0)

        submit_btn = CTkButton(date_window, text="Confirmar", command=self.grab_date)
        submit_btn.place(x=55, y=190)
    
    def grab_date(self):
        self.date.delete(0, END)
        self.date.insert(0, cal.get_date())
        date_window.destroy()

    def pick_time(self, event):
        global time_picker, time_window
        
        time_window = CTkToplevel()
        time_window.grab_set()
        time_window.title('Escolha o horário da aplicação')
        time_window.geometry('380x350')
        time_picker = AnalogPicker(time_window)
        time_picker.place(x=0, y=0)

        submit_btn = CTkButton(time_window, text="Confirmar", command=self.grab_time)
        submit_btn.place(relx=0.32, rely=0.9)
    
    def grab_time(self):
        self.time.delete(0, END)
        self.time.insert(0, time_picker.time())
        time_window.destroy()