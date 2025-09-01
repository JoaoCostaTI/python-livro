import sys

arquivo = sys.argv[1]

with open(arquivo, 'r') as exibicao:
    for l in exibicao:
        print(l)

