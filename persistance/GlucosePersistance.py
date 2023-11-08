from .Banco import Banco
from model.Glucose import Glucose

class GlucosePersistance:
    @classmethod
    def insert_glucose(self, g:Glucose):
        return "Índice glicêmico cadastrado com sucesso!"
        
    @classmethod
    def delete_glucose(self, g:Glucose):
        return True
    
    @classmethod
    def check_instance(self, g:Glucose):
        return True