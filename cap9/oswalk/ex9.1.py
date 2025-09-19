import sys

if len(sys.argv) != 2:
    print('ERRO! Uso: python executavel.py nomeDoArquivo ')
else:

    arquivo = sys.argv[1]

    abertura = open(arquivo, 'r')

    for l in abertura.readlines():
        print(l)

    abertura.close()