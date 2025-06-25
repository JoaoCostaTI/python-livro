sal = float(input('Salário: '))
aumento = 10

if sal > 1250:
    aumento = 10
    reajuste = (sal * aumento) / 100
    salF = sal + reajuste
    print(f'Com aumento de {aumento}% o reajuste foi de R${reajuste:6.2f} tendo o novo salário de R${salF:6.2f}')
if sal <= 1250:
    aumento = 15
    reajuste = (sal * aumento) / 100
    salF = sal + reajuste
    print(f'Com aumento de {aumento}% o reajuste foi de R${reajuste:6.2f} tendo o novo salário de R${salF:6.2f}')