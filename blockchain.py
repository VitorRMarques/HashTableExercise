import time
import hashlib

class Bloco:
    def __init__(self, indice, remetente, destinatario, valor, hash_anterior):
        self.indice = indice
        self.timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        self.remetente = remetente
        self.destinatario = destinatario
        self.valor = valor
        self.hash_anterior = hash_anterior
        self.hash_atual = self._gerar_hash()

    def _gerar_hash(self):
        conteudo = f"{self.indice}{self.timestamp}{self.remetente}{self.destinatario}{self.valor}{self.hash_anterior}"
        return hashlib.sha256(conteudo.encode('utf-8')).hexdigest()

    def __str__(self):
        return (
            f"Bloco {self.indice}:\n"
            f"Transação: {self.remetente} -> {self.destinatario} | Valor: R${self.valor}\n"
            f"Hash Anterior: {self.hash_anterior}\n"
            f"Hash Atual: {self.hash_atual}\n"
        )

class Blockchain:
    def __init__(self):
        self.cadeia = [self._criar_bloco_genesis()]

    def _criar_bloco_genesis(self):
        return Bloco(0, "Sistema", "Banco Central", 0, "0")

    def adicionar_transacao(self, remetente, destinatario, valor):
        ultimo_bloco = self.cadeia[-1]
        novo_bloco = Bloco(len(self.cadeia), remetente, destinatario, valor, ultimo_bloco.hash_atual)
        self.cadeia.append(novo_bloco)

    def mostrar_cadeia(self):
        for bloco in self.cadeia:
            print(bloco)

    def verificar_integridade(self):
        for i in range(1, len(self.cadeia)):
            bloco_atual = self.cadeia[i]
            bloco_anterior = self.cadeia[i - 1]

            if bloco_atual.hash_anterior != bloco_anterior.hash_atual:
                return False
            if bloco_atual.hash_atual != bloco_atual._gerar_hash():
                return False
        return True

if __name__ == "__main__":
    blockchain = Blockchain()

    blockchain.adicionar_transacao("Regina", "Yago", 150)
    blockchain.adicionar_transacao("Bob", "Carol", 75)
    blockchain.adicionar_transacao("Carol", "Daniel", 200)

    print("=== Blockchain de Transações ===")
    blockchain.mostrar_cadeia()
    print("Integridade:", blockchain.verificar_integridade())

    print("\nAlterando o primeiro bloco...")
    blockchain.cadeia[0].valor = 999999
    blockchain.cadeia[0].hash_atual = blockchain.cadeia[0]._gerar_hash()

    print("\n=== Blockchain Após Alteração ===")
    blockchain.mostrar_cadeia()
    print("Integridade:", blockchain.verificar_integridade())
