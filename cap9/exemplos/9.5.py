LARGURA = 79

with open("entrada.txt") as entrada:
    for l in entrada.readlines():
        if l[0] == ";":
            continue
        elif l[0] == ">":
            print(l[1:].rjust(LARGURA))
        elif l[0] == "*":
            print(l[1:].center(LARGURA))
        else:
            print(l)