palavra = {}

for letra in 'abracadabra':
    palavra[letra] = palavra.get(letra, 0) + 1
print(palavra)