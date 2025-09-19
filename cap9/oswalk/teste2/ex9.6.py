LARGURA = 79
QTD = 40

with open("entrada.txt") as entrada:
    for l in entrada.readlines():
        if l[0] == ";":
            continue
        elif l[0] == "=":
            print("=" * QTD)
        elif l[0] == ">":
            print(l[1:].rjust(LARGURA))
        elif l[0] == "*":
            print(l[1:].center(LARGURA))
        elif l[0] == ".":
            input('Deseja continuar? ')
            print()
        else:
            print(l)