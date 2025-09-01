import sys

arquivo = sys.argv[1]
inicio = sys.argv[2]
fim = sys.argv[3]

with open(arquivo, 'r') as exibicao:
    for l in range(inicio+1, fim):
        print(l)