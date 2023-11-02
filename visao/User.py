from .banco import Banco

class Usuarios(object):

    def __init__(self, email="", senha="", tipo=0):
        self.info = {}
        self.email = email
        self.senha = senha
        self.tipo = tipo

    def insertUser(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("insert into usuarios (email, senha, tipo) values ('" + self.email + "', '" + self.senha + "', '" + str(self.tipo) + "')")
            banco.conexao.commit()
            c.close()
            return "Usuário cadastrado com sucesso!"
        except Exception as e:
            return "Ocorreu um erro na inserção do usuário: " + str(e)

    def updateUser(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("update usuarios set email = '" + self.email + "', '" + self.senha + "', '" + self.tipo + "' where email = " + str(self.email))
            banco.conexao.commit()
            c.close()
            return "Usuário atualizado com sucesso!"
        except Exception as e:
            return "Ocorreu um erro na alteração do usuário: " + str(e)

    def deleteUser(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("delete from usuarios where email = " + str(self.email))
            banco.conexao.commit()
            c.close()
            return "Usuário excluído com sucesso!"
        except Exception as e:
            return "Ocorreu um erro na exclusão do usuário: " + str(e)

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
