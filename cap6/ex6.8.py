l = [15,7,27,39]
p = int(input('Valor a procurar: '))
x = 0

while x < len(l):
    if l[x] == p:
        
        break
    x += 1
if x < len(l):
    print(f'{p} localizado na posição {x}')
else:
    print(f'{p} não foi encontrado na lista')