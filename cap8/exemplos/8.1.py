def pesquisa (lista, valor):
    for x, e in enumerate(lista):
        if e == valor:
            return x
    return 'Valor não encontrado'
l = [10,20,25,30]
print(pesquisa(l, 25))
print(pesquisa(l, 27))