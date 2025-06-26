frase = str(input('Frase: '))
listaVogais = ['a','e','i','o','u']
vogaisFinais = []


for c in frase:
    if c in listaVogais:
        vogaisFinais.append(c)

qtdVogais = len(vogaisFinais)
print(f'Vogais encontradas: {qtdVogais}')
print(f'Vogais distintas: {set(vogaisFinais)}')