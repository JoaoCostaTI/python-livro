
codigos = [1,2,3,5,9]

valorTotal = 0

while True:
    print('~' * 30)
    print(f'1 = 0,50\n2 = 1,00\n3 = 4,00\n5 = 7,00\n9 = 8,00')
    print('~' * 30)
    codigoProduto = int(input('Qual produto adicionar? '))
    if codigoProduto == 0:
        break

    if codigoProduto not in codigos:
       print('-' * 30)
       print('Código inválido, selecionar apenas os da lista acima! e 0 PARA SAIR DO PROGRAMA! ') 
       print('-' * 30)
    else:
        qtdComprada = int(input('Quantidade comprada: '))
        if codigoProduto == 1:
            valorTotal += (qtdComprada * 0.50)
        if codigoProduto == 2:
            valorTotal += (qtdComprada * 1.00)
        if codigoProduto == 3:
            valorTotal += (qtdComprada * 4.00)
        if codigoProduto == 5:
            valorTotal += (qtdComprada * 7.00)
        if codigoProduto == 9:
            valorTotal += (qtdComprada * 8.00)
        

print(f'Valor total da compra: R${valorTotal:.2f}')
