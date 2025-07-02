l = [8,9,15]
v = int(input('NUMERO para encontra: '))

for c in l:
    if c == v:
        print(f'{c} encontrado!')
        break
else:
    print('Valor não encontrado na lista')