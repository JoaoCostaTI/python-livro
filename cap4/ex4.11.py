valorCasa = float(input('Valor da casa: '))
salario = float(input('Salário: '))
anosAPagar = int(input('Anos para pagamento: '))

meses = anosAPagar * 12
prestacao = valorCasa / meses

salario30 = (salario * 30) / 100

if prestacao > salario30:
    print(f'EMPRESTIMO NÃO APROVADO! ')
else:
    print(f'EMPRESTIMO APROVADO! ')

print(f'Valor da casa: R${valorCasa:12.2f}')
print(f'Salário: R${salario:10.2f}')
print(f'Prestação R${prestacao:6.2f}')
print(f'30% do Salário R${salario30:.2f}')
