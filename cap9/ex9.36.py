import sys
import os
import os.path
import math

def tamanhoParaHumanos(tamanho):
    if tamanho == 0:
        return "0 byte"
    grandeza = math.log(tamanho, 10)
    if grandeza < 3:
        return f"{tamanho} bytes"
    elif grandeza < 6:
        return f"{tamanho / 1024.0:7.3f} KB"
    elif grandeza < 9:
        return f"{tamanho / pow(1024, 2)} MB"
    elif grandeza < 12:
        return f"{tamanho / pow(1024, 3)} GB"

mascaraDeEstilo = "'margin: 5px 0px 5px %dpx;'"
def geraEstilo(nivel):
    return mascaraDeEstilo % (nivel * 30)

def geraNivelEEstilo(raiz):
    def nivel(caminho):
        xnivel = caminho.count(os.sep) - nraiz
        return geraEstilo()
    nraiz = raiz.count(os.sep)
    return nivel