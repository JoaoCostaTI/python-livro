def soma (lista):
    total = 0
    for valores in lista:
        total += valores
    return total
def media (lista):
    return soma(lista) / len(lista)

l = [2,4,6,8,10]

print(soma(l))
print(media(l))

