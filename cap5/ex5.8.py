n1 = int(input('Numero 1: '))
n2 = int(input('Numero 2: '))

c = 0
acumulador = 0
if n1 < n2:
    while c < n1:
        acumulador += n2
        c += 1
    
else:
    while c < n2:
        acumulador += n1
        c += 1

print(acumulador)