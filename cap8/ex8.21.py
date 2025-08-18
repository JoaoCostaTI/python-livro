def RANGI(inicio= 0, fim=0, salto = 1):
    if fim == 0:
        print(0, 1)
    else:
        for n in range(inicio, fim+1, salto):
            print(n, end= " ")
RANGI(0,10,2)

def faixa(inicio, fim=None, passo=1):
    if fim is None:
        inicio,fim=0, inicio

    atual = inicio
    while atual <= fim:
        yield atual
        atual += passo
print()
print(list(faixa(1,10)))