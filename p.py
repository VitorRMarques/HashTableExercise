import hashlib

tamanho = 10
tabela = [None]* 10



class Usuario: 
    def __init__(self, usuario, senha):
        self.usuario = usuario
        self.senha = senha

    def cadastro(self, senhaRep):
        usuario = input("digite o usuario:")
        senha = input("digite a senha:")
        senhaRep = input("digite a senha novamente:")


        if senha != senhaRep:
            print("Senhas não coincidem")
        else:
            print("Conta cadastrada")
            senha = hashlib.sha256()
            return usuario, senha

    def hashPassword(self):
        return hashlib.sha256(senha.encode()).hexdigest()

    def login(self):
        usuario = input("Digite o usuario")
        senha = input("Digite a senha")
        return usuario, senha


