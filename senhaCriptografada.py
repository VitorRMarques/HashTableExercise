import json
import os
import hashlib
import secrets

class Usuario:
    def __init__(self, nome, email, senha=None, senha_hash=None, salt=None):
        self.nome = nome
        self.email = email.lower().strip()
        if senha is not None:  
            self.salt = secrets.token_hex(16)  
            self.senha_hash = self._hash_senha(senha)
        else:  
            self.salt = salt
            self.senha_hash = senha_hash

    def _hash_senha(self, senha):
        """Gera hash com salt."""
        return hashlib.sha256((self.salt + senha).encode('utf-8')).hexdigest()

    def verificar_senha(self, senha):
        """Verifica senha usando o salt armazenado."""
        return self.senha_hash == hashlib.sha256((self.salt + senha).encode('utf-8')).hexdigest()


class SistemaLogin:
    def __init__(self, arquivo_dados="usuarios.json"):
        self.arquivo_dados = arquivo_dados
        self.usuarios = self._carregar_usuarios()

    def _carregar_usuarios(self):
        if os.path.exists(self.arquivo_dados):
            try:
                with open(self.arquivo_dados, "r", encoding="utf-8") as f:
                    dados = json.load(f)
                    return {
                        email: Usuario(
                            d["nome"], email,
                            senha_hash=d["senha_hash"],
                            salt=d["salt"]
                        )
                        for email, d in dados.items()
                    }
            except (json.JSONDecodeError, KeyError):
                print("Erro ao carregar dados. Criando novo arquivo.")
        return {}

    def _salvar_usuarios(self):
        dados = {
            email: {
                "nome": u.nome,
                "senha_hash": u.senha_hash,
                "salt": u.salt
            }
            for email, u in self.usuarios.items()
        }
        with open(self.arquivo_dados, "w", encoding="utf-8") as f:
            json.dump(dados, f, indent=4, ensure_ascii=False)

    def cadastrar_usuario(self, nome, email, senha):
        email = email.lower().strip()
        if email in self.usuarios:
            print("E-mail já cadastrado!")
            return False
        novo_usuario = Usuario(nome, email, senha)
        self.usuarios[email] = novo_usuario
        self._salvar_usuarios()
        print("Usuário cadastrado com sucesso!")
        return True

    def login(self, email, senha):
        email = email.lower().strip()
        usuario = self.usuarios.get(email)
        if usuario and usuario.verificar_senha(senha):
            print(f"Login bem-sucedido! Bem-vindo(a), {usuario.nome}.")
            return True
        print("E-mail ou senha incorretos.")
        return False


if __name__ == "__main__":
    sistema = SistemaLogin()

    while True:
        print("\n=== MENU ===")
        print("1 - Cadastrar")
        print("2 - Login")
        print("3 - Sair")
        opcao = input("Escolha: ").strip()

        if opcao == "1":
            nome = input("Nome: ")
            email = input("E-mail: ")
            senha = input("Senha: ")
            sistema.cadastrar_usuario(nome, email, senha)

        elif opcao == "2":
            email = input("E-mail: ")
            senha = input("Senha: ")
            sistema.login(email, senha)

        elif opcao == "3":
            print("Encerrando...")
            break
        else:
            print("Opção inválida.")
