from customtkinter import *
from view.RegisterGlucoseScreen import RegisterGlucoseScreen
from view.ListGlucoseScreen import ListGlucoseScreen
from view.RegisterInsulinScreen import RegisterInsulinScreen
from view.RegisterMealScreen import RegisterMealScreen

class UserScreenController:
    @classmethod
    def open_register_glucose(self, email):
        RegisterGlucoseScreen(email)

    @classmethod
    def open_list_glucose(self, email):
        ListGlucoseScreen(email)

    @classmethod
    def open_register_insulin(self, email):
        RegisterInsulinScreen(email)

    @classmethod
    def open_register_meal(self, email):
        RegisterMealScreen(email)