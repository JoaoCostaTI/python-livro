n1 = int(input('N1: '))
n2 = int(input('N2: '))
op = str(input('Qual operação realizar? '))
res = 0

if op == '+':
    res = n1 + n2
elif op == '-':
    res = n1 - n2
elif op == '*':
    res = n1 * n2
elif op == "/":
    res = n1 / n2
else:
    print('Operação inválida, selecione apenas entre [ + - * / ]')
if op not in "/*-+":
    print(f'Resultado = {res}')
else:
    print(f'{n1}{op}{n2}={res}')