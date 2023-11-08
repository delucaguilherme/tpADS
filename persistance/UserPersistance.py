from .Banco import Banco
from model.User import User

class UserPersistance:
    @classmethod
    def insertUser(self, u:User):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("insert into usuarios (email, senha, tipo) values ('" + u.email + "', '" + u.password + "', '" + str(u.type) + "')")
            banco.conexao.commit()
            c.close()
            print("cadastrado: " + u.email + " " + u.type)
            return "Usuário cadastrado com sucesso!"
        except Exception as e:
            return "Ocorreu um erro na inserção do usuário: " + str(e)
        
    @classmethod
    def deleteUser(self, u:User):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("delete from usuarios where email = " + str(u.email))
            banco.conexao.commit()
            c.close()
            return "Usuário excluído com sucesso!"
        except Exception as e:
            return "Ocorreu um erro na exclusão do usuário: " + str(e)
        
    @classmethod
    def test(self, u:User):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute('select * from usuarios where email = ? and senha= ?', (u.email, u.password))
            result = c.fetchone()
            #print("aqui: " + str(result))
            c.close()
            if result != None:
                return result[2]
            else:
                return 2
        except Exception as e:
            return "erro na busca do usuário: " + str(e)
