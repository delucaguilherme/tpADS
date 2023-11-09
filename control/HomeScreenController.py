from customtkinter import *

from view.UserScreen import UserScreen
from view.AdminScreen import AdminScreen
from view.RegisterUserScreen import RegisterUserScreen

from model.User import User
from persistance.UserPersistance import UserPersistance

class HomeScreenController:
    @classmethod
    def signin_user(self, screen):
        email = screen.email.get()
        password = screen.password.get()

        user = User(email, password)
        result = UserPersistance.test(user)
        #print("result", result)

        if result == 0:
            UserScreen(email)
        elif result == 1:
            AdminScreen(email)
        else:
            self.wrong_credentials(screen)

    @classmethod
    def wrong_credentials(self, screen):
        message = CTkLabel(
            master=screen.get_root(), 
            text='Usuário ou senha incorretos!', 
            text_color='red', 
            font=('Segeo UI', 16, 'bold'))
        message.place(relx='0.5', rely='0.76', anchor=CENTER)

    @classmethod
    def open_register_user_screen(self):
        RegisterUserScreen()
