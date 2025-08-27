import sys

if len(sys.argv) != 4:
    print('ERRO! use: python ex9.2.py nomeDoArquivo inicio fim...')
else:
    inicio = int(sys.argv[2]) 
    fim = int(sys.argv[3])
    nome = sys.argv[1]

    imprimir = open(nome, 'r')

    for l in imprimir.readlines()[inicio-1:fim]:
        print(l)
    imprimir.close()