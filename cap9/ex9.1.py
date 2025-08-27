import sys

if len(sys.argv) != 2:
    print(f'Argumentos incorretos, escreva 2 argumentos!\nExemplo: python ex9.1.py nomeDoArquivo')
else:
    arquivo = sys.argv[1]
    teste = open(arquivo, 'r')

    for l in teste:
        print(l[:-1])
    teste.close()

