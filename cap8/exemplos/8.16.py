def imprimeMaior(mensagem, *num):
    print(num)
    maior = 0

    for n in num:
        if n > maior:
            maior = n
    return print(f'{mensagem}: {maior}')

imprimeMaior('Maior',2,4,5,2,2,19,2,2,4)
imprimeMaior('Max',2,4,5,2,9,2,2,4)
imprimeMaior('Max')