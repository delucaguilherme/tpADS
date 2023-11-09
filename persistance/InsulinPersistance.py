from .Banco import Banco
from model.Insulin import Insulin

class InsulinPersistance:
    @classmethod
    def insertInsulin(self, i:Insulin):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("insert into insulina (quantity, type, date, time, meal_type, meal_time, usuario) values ('" + i.quantity + "', '" + i.type + "', '" + i.date + "', '" + i.time + "', '" + i.meal_type + "', '" + i.meal_time + "', '" + i.usuario + "')")
            banco.conexao.commit()
            c.close()
            print("cadastrado: " + i.quantity + " " + i.type + " " + i.date + " " + i.time + " " + i.meal_type + " " + i.meal_time + " " + i.usuario)
            return "Aplicação de insulina registrada com sucesso!"
        except Exception as e:
            return "Ocorreu um erro no registro da aplicação de insulina: " + str(e)
        
    @classmethod
    def deleteInsulin(self, id):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("DELETE FROM insulina WHERE id = ?", + (id,))
            banco.conexao.commit()
            # Verifique se algum registro foi afetado
            if c.rowcount > 0:
                c.close()
                return "Registro de insulina excluído com sucesso!"
            else:
                c.close()
                return "Registro não encontrado."
        except Exception as e:
            return "Ocorreu um erro na exclusão do registro de aplicação de insulina: " + str(e)
        
    @classmethod
    def selectAll(self):
        banco = Banco()
        try:
            i = 0
            c = banco.conexao.cursor()
            c.execute("SELECT * FROM insulina")

            cadastrados = c.fetchall()
            if cadastrados:
                print("Consulta executada com sucesso!")
            else:
                print("Nenhum registro de insulina cadastrado.")
            return cadastrados
        except Exception as e:
            return "Ocorreu um erro: " + str(e)