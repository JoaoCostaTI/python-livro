
lista = [3,3,1,5,4]

x = len(lista)

for algo in range(len(lista)):
    i = 0
    for c in range(x):
        if i == x-1:
            break
        elif lista[i] > lista[i+1]:
            temp = lista[i]
            lista[i] = lista[i+1]
            lista[i+1] = temp
        i += 1
print(lista)