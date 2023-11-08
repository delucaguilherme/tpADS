from .Banco import Banco
from model.Meal import Meal

class MealPersistance:
    @classmethod
    def insert_meal(self, m:Meal):
        return True
        
    @classmethod
    def delete_meal(self, m:Meal):
        return True
    
    @classmethod
    def test(self, m:Meal):
        return True
    