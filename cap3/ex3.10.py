salarioAtual = float(input('Salário: '))
aumento = int(input('Aumento: '))
salarioF = salarioAtual + (salarioAtual*aumento/100)

print(f'Com {aumento}% de aumento o novo salário será: R${salarioF:.2f}')