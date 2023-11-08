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
        
    # @classmethod
    # def deleteUser(self, u:User):
    #     banco = Banco()
    #     try:
    #         c = banco.conexao.cursor()
    #         c.execute("delete from usuarios where email = " + str(u.email))
    #         banco.conexao.commit()
    #         c.close()
    #         return "Usuário excluído com sucesso!"
    #     except Exception as e:
    #         return "Ocorreu um erro na exclusão do usuário: " + str(e)

    # @classmethod
    # def selectUser(self, email, password):
    #     banco = Banco()
    #     try:
    #         c = banco.conexao.cursor()
    #         c.execute("SELECT * FROM usuarios WHERE email = ? and senha = ?", (email,password))
    #         result = c.fetchone()
    #         if result:
    #             self.email = result[0]
    #             self.senha = result[1]
    #             self.tipo = result[2]
    #             c.close()
    #             return self.tipo
    #         else:
    #             c.close()
    #             return "Usuário ou senha incorretos."
    #     except Exception as e:
    #         return "Ocorreu um erro na busca do usuário: " + str(e)
        
    # @classmethod
    # def test(self, u:User):
    #     banco = Banco()
    #     try:
    #         c = banco.conexao.cursor()
    #         c.execute('select * from usuarios where email = ? and senha= ?', (u.email, u.senha))
    #         result = c.fetchone()
    #         #print("aqui: " + str(result))
    #         c.close()
    #         if result != None:
    #             return result[2]
    #         else:
    #             return 2
    #     except Exception as e:
    #         return "erro na busca do usuário: " + str(e)
        
