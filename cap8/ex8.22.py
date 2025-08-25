import math
import operator
from functools import partial


def executa_unário(operação, símbolo, operando1):
    resultado = operação(float(operando1))
    print(f"{símbolo} {operando1} = {resultado}")


def executa(operação, símbolo, operando1, operando2):
    resultado = operação(float(operando1), float(operando2))
    print(f"{operando1} {símbolo} {operando2} = {resultado}")


operações = {
    "+": partial(executa, operator.add, "+"),
    "-": partial(executa, operator.sub, "-"),
    "*": partial(executa, operator.mul, "×"),
    "/": partial(executa, operator.truediv, "÷"),
    "raiz": partial(executa_unário, math.sqrt, "raiz quadrada de "),
    "potência": partial(executa, operator.pow, "potência"),
}
operando1 = input("Operador 1: ")
operação = input("Operação: ").strip().lower()
if operação in operações:
    if operação == "raiz":  # Raiz tem apenas um operador
        operações[operação](operando1)
    else:
        operando2 = input("Operador 2: ")
        operações[operação](operando1, operando2)
else:
    print("Operação inválida!")