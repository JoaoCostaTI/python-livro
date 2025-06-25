soma = 0
c = 0

while True:
    n = int(input('Digite um numero: (0 para sair do programa)'))

    if n == 0:
        break

    soma += n
    c += 1

print(f'Foram digitados {c} numeros, A soma de todos é {soma} e a média aritmética é {soma/c:.2f}')