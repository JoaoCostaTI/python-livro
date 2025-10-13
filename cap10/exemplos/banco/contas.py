class Conta:
    def __init__(self, clientes,numero, saldo=0):
        self.saldo = 0
        self.clientes = clientes
        self.numero = numero
        self.operacoes = []
        self.deposito(saldo)

    def resumo(self):
        print(f"CC Nº:{self.numero}\nSaldo: R${self.saldo:.2f}")
        print('-' * 15)
        for cliente in self.clientes:
            print(f"Nome: {cliente.nome}\nTelefone:{cliente.telefone}")

    def saque(self,valorSaque):
        if self.saldo >= valorSaque:
            self.saldo -= valorSaque
            self.operacoes.append(["SAQUE", valorSaque])
        else:
            print(f'Saldo insuficiente, você tem {self.saldo:.2f}')

    def deposito(self,valorDeposito):
        self.saldo += valorDeposito
        self.operacoes.append(['DEPOSITO', valorDeposito])

    def extrato(self):
        print(f'Extrato CC nº: {self.numero}\n')
        for op in self.operacoes:
            print(f'{op[0]} {op[1]:.2f}')
        print(f"\nSaldo: R${self.saldo:.2f}\n")

class ContaEspecial(Conta):
    def __init__(self, clientes, numero, saldo=0, limite=0):
        super().__init__(clientes, numero, saldo)
        self.limite = limite
    
    def saque(self, valor):
        if self.saldo + self.limite >= valor:
            self.saldo -= valor
            self.operacoes.append(['SAQUE', valor])

