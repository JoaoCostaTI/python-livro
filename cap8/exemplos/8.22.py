import random

n = random.randint(1,10)

x = int(input('Digite um numero entre 1 e 10: '))

if x == n:
    print(f'Você acertou!\nSeu numero: {x}\nNumero do computador: {n}')
else:
    print(f'Você Errou!\nSeu numero: {x}\nNumero do computador: {n}')