def bytesLittlesEndian(numero, nbytes = 4, sinal = False):
    """
    Converta um numero inteiro para uma sequencia de butes usando a codigicação little endian.
    Se sinal for passado, reserva um bit para representar o sinal."""
    return numero.to_bytes(nbytes, "little", signed = sinal)

def padding(valor, tamanho=4):
    """Calcula o próximo multiplo para tamanho"""
    if resto := valor % tamanho:
        return valor + tamanho - resto
    return valor