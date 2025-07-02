l = [15,7,27,39]
p = int(input('Valor a procurar: '))
achou = False
x = 0

while x < len(l):
    if l[x] == p:
        achou = True
        break
    x += 1
if achou:
    print(f'{p} localizado na posição {x}')
else:
    print(f'{p} não encontrado ')