from view.RegisterAdminScreen import RegisterAdminScreen
from view.DeleteScreen import DeleteScreen

class AdminScreenController:
    @classmethod
    def open_register_admin_screen(self):
        RegisterAdminScreen()

    @classmethod
    def open_delete_screen(self):
        DeleteScreen()

    