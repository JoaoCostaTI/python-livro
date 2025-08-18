def faixa(inicio, fim=None, passo=1):
    if fim is None:
        inicio, fim = 0, inicio

    atual = inicio
    while atual <= fim:  # Observe o <= para incluir o último valor
        yield atual
        atual += passo


# Casos de teste
print(list(faixa(1)))  # [0, 1]
print(list(faixa(1, 10)))  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(faixa(0, 10, 2)))  # [0, 2, 4, 6, 8, 10]