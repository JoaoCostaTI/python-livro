l = [15,7,27,39]
p1 = int(input('Valor UM a procurar: '))
p2 = int(input('Valor DOIS a procurar: '))
x1 = 0

while x1 < len(l):
    if l[x1] == p1:  
        break
    x1 += 1
if x1 < len(l):
    print(f'{p1} localizado na posição {x1}')
else:
    print(f'{p1} não foi encontrado na lista')

x2 = 0
while x2 < len(l):
    if l[x2] == p2:  
        break
    x2 += 1
if x2 < len(l):
    print(f'{p2} localizado na posição {x2}')
else:
    print(f'{p2} não foi encontrado na lista')

print('-'*10)

primeiro = segundo = 0

if x1 < x2:
    print(f'{p1} foi encontrado primeiro na posição {x1}\n{p2} encontrado depois na posição {x2}')
else:
    print(f'{p2} foi encontrado primeiro na posição {x2}\n{p1} encontrado depois na posição {x1}')