from .Banco import Banco
from model.Glucose import Glucose

class GlucosePersistance:
    @classmethod
    def insertGlucose(self, g:Glucose):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("insert into indice_glicemico (sugar_level, date, time, meal_type, meal_time, usuario) values ('" + g.sugar_level + "', '" + g.date + "', '" + g.time + "', '" + g.meal_type + "', '" + g.meal_time + "', '" + g.usuario + "')")
            banco.conexao.commit()
            c.close()
            print("cadastrado: " + g.sugar_level + " " + g.date + " " + g.time + " " + g.meal_type + " " + g.meal_time + " " + g.usuario)
            return "Índice glicêmico registrado com sucesso!"
        except Exception as e:
            return "Ocorreu um erro no registro de índice glicêmico: " + str(e)
        
    @classmethod
    def deleteGlucose(self, id):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("DELETE FROM indice_glicemico WHERE id = ?", + (id,))
            banco.conexao.commit()
            # Verifique se algum registro foi afetado
            if c.rowcount > 0:
                c.close()
                return "Registro de índice glicêmico excluído com sucesso!"
            else:
                c.close()
                return "Registro não encontrado."
        except Exception as e:
            return "Ocorreu um erro na exclusão do registro de índice glicêmico: " + str(e)
    
    @classmethod
    def selectAll(self, email):
        banco = Banco()
        try:
            i = 0
            c = banco.conexao.cursor()
            c.execute("SELECT * FROM indice_glicemico WHERE usuario = ?", + (email,))

            cadastrados = c.fetchall()
            if cadastrados:
                print("Consulta executada com sucesso!")
            else:
                print("Nenhum registro de índice glicêmico cadastrado.")
            return cadastrados
        except Exception as e:
            return "Ocorreu um erro: " + str(e)