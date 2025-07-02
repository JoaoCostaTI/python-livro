lista1 = [0,1,1,2,2,4,4,8,8]
lista2 = [0,1,2,3,4,5,5,6,7,7]

lista3 = []

x = 0

while x < len(lista1):
    if lista1[x] not in lista3:
        lista3.append(lista1[x])
    x += 1
x = 0
while x < len(lista2):
    if lista2[x] not in lista3:
        lista3.append(lista2[x])
    x += 1
x = 0

while x < len(lista3):
    print(f'{x} = {lista3[x]}')
    x += 1