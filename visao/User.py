from .banco import Banco

class Usuarios(object):

    def __init__(self, idusuario=0, nome="", email="", usuario="", senha=""):
        self.info = {}
        self.idusuario = idusuario
        self.nome = nome
        self.email = email
        self.usuario = usuario
        self.senha = senha

    def insertUser(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("insert into usuarios (nome, email, usuario, senha) values ('" + self.nome + "', '" + self.email + "', '" + self.usuario + "', '" + self.senha + "')")
            banco.conexao.commit()
            c.close()
            return "Usuário cadastrado com sucesso!"
        except Exception as e:
            return "Ocorreu um erro na inserção do usuário: " + str(e)

    def updateUser(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("update usuarios set nome = '" + self.nome + "', email = '" + self.email + "', usuario = '" + self.usuario + "', senha = '" + self.senha + "' where idusuario = " + str(self.idusuario))
            banco.conexao.commit()
            c.close()
            return "Usuário atualizado com sucesso!"
        except Exception as e:
            return "Ocorreu um erro na alteração do usuário: " + str(e)

    def deleteUser(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("delete from usuarios where idusuario = " + str(self.idusuario))
            banco.conexao.commit()
            c.close()
            return "Usuário excluído com sucesso!"
        except Exception as e:
            return "Ocorreu um erro na exclusão do usuário: " + str(e)

    def selectUser(self, idusuario):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("select * from usuarios where idusuario = " + str(idusuario))
            for linha in c:
                self.idusuario = linha[0]
                self.nome = linha[1]
                self.email = linha[2]
                self.usuario = linha[3]
                self.senha = linha[4]
            c.close()
            return "Busca feita com sucesso!"
        except Exception as e:
            return "Ocorreu um erro na busca do usuário: " + str(e)
