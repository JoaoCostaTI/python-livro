def faixaInt(pergunta, min, max):
    while True:
        v = int(input(pergunta))
        if v < min or v > max:
            print(f'Inválido! Digite um valor entre {min} e {max}')
        else:
            return v
            
faixaInt('Digite um numero entre 0 e 10', 0, 10)