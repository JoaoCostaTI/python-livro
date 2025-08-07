def imprimeLista(l, fimpressao, fcondicao):
    for e in l:
        if fcondicao(e):
            fimpressao(e)

def imprimeElemento(e):
    print(f'Valor: {e}')

def epar(x):
    return x % 2 == 0

def eimpar(x):
    return not epar(x)

l = [1,7,9,2,11,0]

imprimeLista(l, imprimeElemento, epar)
imprimeLista(l, imprimeElemento, eimpar)