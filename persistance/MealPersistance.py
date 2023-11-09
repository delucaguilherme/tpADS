from .Banco import Banco
from model.Meal import Meal

class MealPersistance:
    @classmethod
    def insert_meal(self, m:Meal):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("insert into refeicao (carbohydrates, date, time, meal_type, usuario) values ('" + m.carbohydrates + "', '" + m.date + "', '" + m.time + "', '" + m.meal_type + "', '" + m.usuario + "')")
            banco.conexao.commit()
            c.close()
            print("cadastrado: " + m.carbohydrates + " " + m.date + " " + m.time + " " + m.meal_type + " " + m.usuario)
            return "Refeição registrada com sucesso!"
        except Exception as e:
            return "Ocorreu um erro no registro da refeição: " + str(e)
        
    @classmethod
    def deleteMeal(self, id):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("DELETE FROM refeicao WHERE id = ?", (id,))
            banco.conexao.commit()
            # Verifique se algum registro foi afetado
            if c.rowcount > 0:
                c.close()
                return "Registro de refeição excluído com sucesso!"
            else:
                c.close()
                return "Registro não encontrado."
        except Exception as e:
            return "Ocorreu um erro na exclusão do registro de refeição: " + str(e)
    
    @classmethod
    def selectAll(self):
        banco = Banco()
        try:
            i = 0
            c = banco.conexao.cursor()
            c.execute("SELECT * FROM refeicao")

            cadastrados = c.fetchall()
            if cadastrados:
                print("Consulta executada com sucesso!")
            else:
                print("Nenhum registro de refeição cadastrado.")
            return cadastrados
        except Exception as e:
            return "Ocorreu um erro: " + str(e)