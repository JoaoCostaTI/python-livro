import sys

arquivo = sys.argv[1]
inicio = int(sys.argv[2])
fim = int(sys.argv[3])

with open(arquivo, 'r') as exibicao:
    for l in exibicao.readlines()[inicio -1 : fim]:
        print(l)