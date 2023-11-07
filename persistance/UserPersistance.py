from .Banco import Banco
from model.User import User

class UserPersistance:
    @classmethod
    def insertUser(self, u:User):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("insert into usuarios (email, senha, tipo) values ('" + u.email + "', '" + u.senha + "', '" + str(u.tipo) + "')")
            banco.conexao.commit()
            c.close()
            print("cadastrado: " + u.email + " " + u.senha)
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
    def selectUser(self, email, password):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("SELECT * FROM usuarios WHERE email = ? and senha = ?", (email,password))
            result = c.fetchone()
            if result:
                self.email = result[0]
                self.senha = result[1]
                self.tipo = result[2]
                c.close()
                return self.tipo
            else:
                c.close()
                return "Usuário ou senha incorretos."
        except Exception as e:
            return "Ocorreu um erro na busca do usuário: " + str(e)
        
    @classmethod
    def test(self, u:User):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute('select * from usuarios where email = ? and senha= ?', (u.email, u.senha))
            result = c.fetchone()
            #print("aqui: " + str(result))
            c.close()
            if result != None:
                return result[2]
            else:
                return 2
        except Exception as e:
            return "erro na busca do usuário: " + str(e)
        
