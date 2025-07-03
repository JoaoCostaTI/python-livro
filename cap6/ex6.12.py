l = [9,7,2,4]
maior = menor = l[0]

for e in l:
    if e > maior:
        maior = e
    if e < menor:
        menor = e
print(maior)
print(menor)