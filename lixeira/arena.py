listaDeCompras = ["maçã", "pão", "leite", "maçã", "arroz", "pão"]
dicionarioListaCompras = {}

for p, itens in enumerate(listaDeCompras, start=1):
    if itens not in dicionarioListaCompras:
        dicionarioListaCompras[itens] = [p]
    else:
        dicionarioListaCompras[itens] += [p]
    
print(dicionarioListaCompras)