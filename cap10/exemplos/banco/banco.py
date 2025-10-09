class Banco:
    def __init__(self, nome):
        self.nome = nome
        self.contas = []
    def abreConta(self, conta):
        self.contas.append(conta)
    def listaContas(self):
        for conta in self.contas:
            conta.resumo()