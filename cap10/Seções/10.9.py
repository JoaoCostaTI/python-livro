'''
class BancoException(Exception):
    pass

class SaldoIndisponivel(BancoException):
    print('Chegou aq')
    pass

class ClienteNaoExiste(BancoException):
    pass

def saque(saldo, valor):
    if valor > saldo:
        raise SaldoIndisponivel
    return saldo - valor

try:
    saldo = saque(100, 500)
except SaldoIndisponivel:
    print('Erro: Saldo insuficiente! ')
'''

class EstoqueException(Exception):
    def __init__(self, mensagem, codigo_do_erro):
        super().__init__(mensagem)
        self.codigo_do_erro = codigo_do_erro

def verifique_quantidade(quantidade):
    if quantidade < 0:
        raise EstoqueException('Quantidade negativa', codigo_do_erro=1)
    
try:
    verifique_quantidade(-10)
except EstoqueException as e:
    print(f'Erro: {e.codigo_do_erro} {e}')
