import sys

arquivo = sys.argv[1]
fraseSplit = ""
fraseFinal = ""
dicionarioFrase = {}

with open(arquivo, 'r', encoding="utf-8") as frase:
    for item in frase.readlines():
        fraseSplit += item
    fraseFinal =  fraseSplit.split()
    
for k, v in enumerate(fraseFinal):
    if v not in dicionarioFrase:
        dicionarioFrase[v] = 1
    else:
        dicionarioFrase[v] += 1


for k, v in dicionarioFrase.items():
    print(f"{k} = {v}")