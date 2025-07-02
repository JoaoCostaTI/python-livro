lista1 = [1,2,3,4,5]
lista2 = [6,7,8,9,10]

lista3 = []

lista3.extend(lista1)
lista3.extend(lista2)

x = 0

while x < len(lista3):
    print(f'{x} = {lista3[x]}')
    x += 1
