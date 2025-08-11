from entrada import validaInteiro

l = []

for x in range(10):
    l.append(validaInteiro('Digite um numero: ', 0, 20))
print(f'Soma: {sum(l)}')