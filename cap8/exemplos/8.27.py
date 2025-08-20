import operator

def executa(operacao, simbolo, operando1, operando2):
    resultado = operacao(float(operando1), float(operando2))
    print(f'{operando1} {simbolo} {operando2} = {resultado}')

    operando1 = input('Operador 1: ')
    operando2 = input('Operador 2: ')
    operacao = input('Operação: ').strip()

    if operacao == "+":
        executa(operator.add, operacao, operando1, operando2)
    elif operacao == "-":
        executa(operator.sub, operacao, operando1, operando2)
    elif operacao == "*":
        executa(operator.mul, operacao, operando1, operando2)
    elif operacao == "/":
        executa(operator.truediv, operacao, operando1, operando2)
        