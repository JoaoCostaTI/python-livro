import sys

arquivo = sys.argv[1]

fraseCompleta = ""
fraseDicionario = {}

with open(arquivo, 'r', encoding="utf-8") as frase:
    for l in frase.readlines():
        fraseCompleta += l

fraseSplit = fraseCompleta.split()

for l in fraseSplit:
    if l not in fraseDicionario:
        fraseDicionario[l] = 1
    else:
        fraseDicionario[l] += 1

print(fraseDicionario)


