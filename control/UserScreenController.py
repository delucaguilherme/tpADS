from customtkinter import *
from view.RegisterGlucoseScreen import RegisterGlucoseScreen
from view.ListGlucoseScreen import ListGlucoseScreen
from view.RegisterInsulinScreen import RegisterInsulinScreen
from view.RegisterMealScreen import RegisterMealScreen
from view.ListInsulinaScreen import ListInsulinaScreen
from view.ListMealScreen import ListMealScreen

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

    @classmethod
    def open_list_insulin(self, email):
        ListInsulinaScreen(email)

    @classmethod
    def open_list_meat(self, email):
        ListMealScreen(email)
        