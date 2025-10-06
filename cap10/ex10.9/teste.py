from contas import Conta
from contas import Cliente

joao = Cliente('João Marcos Mendes Costa', '31992206233')
cleide = Cliente('Cleideane Silva Costa', '3194139158')

conta = Conta([joao, cleide], 1234, 5000)

conta.resumo()

