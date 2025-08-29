import sys

arquivo = sys.argv[1]

texto = open(arquivo, 'r')

for l in texto.readlines():
    print(l[:-1])
texto.close()
