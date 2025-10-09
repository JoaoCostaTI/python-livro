from contas import Conta
from clientes import Cliente
from banco import Banco

joao = Cliente('João Marcos Mendes Costa', '31992206233')
cleide = Cliente('Cleideane Silva Costa', '3194139158')
jose = Cliente('José Silva', 892734590)

contaJC = Conta([joao, cleide], 100)
contaJ = Conta([jose], 10)
tatu = Banco('Tatu')
tatu.abreConta(contaJC)
tatu.abreConta(contaJ)
contaJC.deposito(1000)
contaJ.deposito(500)
contaJC.saque(40.54)
tatu.listaContas()

