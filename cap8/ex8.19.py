def primos(n):
    p = 1  # Posição na sequencia
    yield 2  # 2 é o único primo que é par
    d = 3  # divisor começa com 3
    b = 3  # dividendo começa com 3, é o número que testaremos ser primo ou não
    while p < n:
        # print(d, b, d % b, p, n)
        if b % d == 0:  # Se b é divisível por d, o resto será 0
            if b == d:  # Se b igual a d, todos os valores d já foram testados
                yield b  # b é primo
                p += 1  # incrementa a sequencia
            b += 2  # Passa para o próximo número ímpar
            d = 3  # Recomeça a dividir por 3
        elif d < b:  # Continua tentando?
            d += 2  # Incrementa o divisor para o próximo ímpar
        else:
            b += 2  # Tenta outro número ímpar


for primo in primos(10):
    print(primo)