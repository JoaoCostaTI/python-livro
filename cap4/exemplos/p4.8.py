categoria = int(input('Categoria do produto: '))
if categoria == 1:
    preco = 10
else:
    if categoria == 2:
        preco = 18
    else:
        if categoria == 3:
            preco = 23
        else:
            if categoria == 4:
                preco = 26
            else:
                if categoria == 5:
                    preco = 31
                else: 
                    print(f'Erro, digite um valor entre 1 e 5! ')
                    preco = 0
print(f'Preço do produto: R${preco:6.2f}')