import operator
from functools import partial
import math

def executaUnario(operacao, simbolo, operando1):
    resultado = operacao(float(operando1))
    print(f'{simbolo} {operando1} = {resultado}')

def executa(operacao, simbolo, operando1, operando2):
    resultado = operacao(float(operando1), float(operando2))
    print(f'{operando1} {simbolo} {operando2} = {resultado}')

    operacoes = {
        "+": partial(executa, operator.add, "+"),
        "-": partial(executa, operator.sub, "-"),
        "*": partial(executa, operator.mul, "*"),
        "/": partial(executa, operator.truediv, "/"),
        "raiz": partial(executaUnario, math.sqrt, "raiz quadrada de "),
        "potencia": partial(executa,operator.pow, "potencia de ")
    }

    operando1 = input('Operador 1: ')
    operando2 = input('Operador 2: ')
    operacao = input('Operação: ').strip()

    if operacao in operacoes:
        operacoes[operacao](operando1, operando2)
    else:
        print('Operação inválida! ') 

executa("raiz", "raiz quadrada de ", 9)