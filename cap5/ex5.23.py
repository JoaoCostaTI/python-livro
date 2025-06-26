n = int(input('Numero: '))

if n == 0 or n == 1:
    print('Não é primo')
else:
    if n == 2:
        print('2 é primo')
    elif n % 2 == 0:
        print(f'{n} não é primo, pois 2 é o unico numero primo par.')
    else:
        x = 3
        while x < n:
            if n % x == 0:
                break
            x += 2
        if x == n:
            print(f'{n} é primo')
        else:
            print(f'{n} não é primo, pois é divisível por {x}')