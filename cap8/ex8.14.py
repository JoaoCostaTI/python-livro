import random

n = random.randint(1,5)


print('Tente acertar o numero escolhido pelo computador')
for chances in range(3):
    try:
        x = int(input(f'Digite um numero [Tentativa {chances + 1}]: '))
        if x == n:
            print(f'Você acertou!\nSeu numero: {x}\nNumero do computador: {n}')
            break
        else:
            print(f'Você ERROU! Tente novamente.')
    except ValueError:
        print('Digite apenas numeros entre 0 e 5')

print(f'Seu ultimo numero: {x}\nNumero do computador: {n}')