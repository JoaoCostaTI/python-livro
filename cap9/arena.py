def escritaEmTXT():
    lista = open("algumacoisa.txt", 'w')

    for l in range(1,10):
        lista.write(f"{l}º linha escrita...\n")
    lista.close()

def leituraEmTXT():
    lista = open("algumacoisa.txt", 'r')

    for l in lista.readlines():
        print(f"{l}")
    lista.close()

