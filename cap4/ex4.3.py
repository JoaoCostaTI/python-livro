v1 = int(input('Valor 1: '))
v2 = int(input('Valor 2: '))
v3 = int(input('Valor 3: '))

maior = v1
menor = v1

if v2 > maior:
    maior = v2
if v3 > maior:
    maior = v3
if v2 < menor:
    menor = v2
if v3 < menor:
    menor = v3
print(f'Maior = {maior} --- Menor = {menor}')