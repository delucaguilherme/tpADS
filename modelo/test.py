from administrator import Administrator
from commonUser import CommonUser
import pickle

controle = 1

def cadastrar():
    lista = []

    controle = 1
    while controle == 1:
        username = input("username: ")
        password = input("password: ")
        usuario = CommonUser(username, password)
        lista.append(usuario)

        controle = int(input("Deseja cadastrar mais algum usuário? "))

    with open("users.pkl", "wb") as arquivo:
        pickle.dump(lista, arquivo)

def ler():
    with open("users.pkl", "rb") as arquivo:
        lista = pickle.load(arquivo)
    
    for user in lista:
        print(user)

cadastrar()
ler()

"""
with open("users.pkl", "wb") as arquivo:
    pickle.dump(lista, arquivo)

with open("users.pkl", "rb") as arquivo:
    nova_lista = pickle.load(arquivo)
    for objeto in lista:
        print(objeto)
"""