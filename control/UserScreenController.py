from customtkinter import *
from view.RegisterGlucoseScreen import RegisterGlucoseScreen

class UserScreenController:
    @classmethod
    def open_register_glucose(self, email):
        RegisterGlucoseScreen(email)
