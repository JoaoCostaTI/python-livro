from clientes import Cliente
from contas import Conta, ContaEspecial

joao = Cliente('João Mendes', 92206233)
cleide = Cliente('Cleideane', 94139158)

conta1 = Conta([joao], 3333, 1000)
conta2 = ContaEspecial([joao, cleide], 6666, 500, 1000)

conta1.saque(50)
conta2.deposito(300)
conta1.saque(190)
conta2.deposito(95.15)
conta2.saque(1500)
conta1.extrato()
conta2.extrato()
