arquivo = open('numeros.txt', 'r')

for l in arquivo.readlines():
    print(l)
print(arquivo)
arquivo.close()

