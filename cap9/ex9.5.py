import sys

arquivo = sys.argv[1]

with open(arquivo, 'r') as elementos:
    lista = elementos.readlines()
    
    listaOrdenada = []
    for l in lista:
        listaOrdenada.append(l[:-1])
    listaFinal = []
    for k, v in enumerate(listaOrdenada):
        listaFinal.append(int(v))
    listaFinal.sort(reverse=True)

with open("paresOrdenados.txt", 'w') as paresOrdenados:
    for l in listaFinal:
        paresOrdenados.write(f"{str(l)}\n")