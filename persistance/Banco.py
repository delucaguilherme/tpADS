import sqlite3

class Banco:
    def __init__(self):
        self.conexao = sqlite3.connect('banco.db')
        self.createTable()

    def createTable(self):
        c = self.conexao.cursor()

        c.execute("""create table if not exists usuarios (
                    email primary key,
                    senha text,
                    tipo integer)""")

#        c.execute("""create table if not exists meal (
#                  email primary key,
#                  carboidrates text,
#                  date text, 
#                  type text,
#                  meal text)""")

#        c.execute("""create table if not exists glucose (
#                  email primary key,
#                  sugar_level text,
#                  date text,
#                  time text, 
#                  meal_type text,
#                  meal_time text)""")

        self.conexao.commit()
        c.close()

#Para iniciar uma nova instância do banco, é necessário excluir o atual, descomentar a linha abaixo e rodar apenas este arquivo
"""if __name__ == "__main__":
   Banco()"""