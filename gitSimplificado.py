import hashlib
import time

class Commit:
    def __init__(self, mensagem, conteudo, pai=None):
        self.mensagem = mensagem
        self.conteudo = conteudo
        self.pai = pai  
        self.timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        self.hash = self._gerar_hash()

    def _gerar_hash(self):
        dados = f"{self.mensagem}{self.conteudo}{self.pai}{self.timestamp}"
        return hashlib.sha1(dados.encode('utf-8')).hexdigest()

    def __str__(self):
        return f"Commit: {self.hash[:7]} | {self.mensagem} | {self.timestamp}"


class MiniGit:
    def __init__(self):
        self.commits = {} 
        self.head = None   

    def commit(self, mensagem, conteudo):
        novo_commit = Commit(mensagem, conteudo, self.head)
        self.commits[novo_commit.hash] = novo_commit
        self.head = novo_commit.hash
        print(f"Commit criado: {novo_commit.hash[:7]}")

    def log(self):
        if not self.head:
            print("Nenhum commit encontrado.")
            return
        atual = self.head
        while atual:
            commit = self.commits[atual]
            print(commit)
            atual = commit.pai

    def mostrar_head(self):
        if self.head:
            print(f"HEAD -> {self.commits[self.head]}")
        else:
            print("Nenhum commit no repositório.")


if __name__ == "__main__":
    repo = MiniGit()

    while True:
        print("\n=== MINI GIT ===")
        print("1 - Commit")
        print("2 - Log")
        print("3 - Mostrar HEAD")
        print("0 - Sair")
        opcao = input("Escolha: ").strip()

        if opcao == "1":
            msg = input("Mensagem do commit: ")
            conteudo = input("Conteúdo do arquivo: ")
            repo.commit(msg, conteudo)

        elif opcao == "2":
            repo.log()

        elif opcao == "3":
            hash_commit = input("Digite o hash do commit: ").strip()
            repo.checkout(hash_commit)

        elif opcao == "4":
            repo.mostrar_head()

        elif opcao == "0":
            print("Encerrando...")
            break
        else:
            print("Opção inválida.")
