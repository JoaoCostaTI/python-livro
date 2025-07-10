palavra = {}

for letra in 'abracadabra':
    if letra in palavra:
        palavra[letra] += 1
    else:
        palavra[letra] = 1
print(palavra)