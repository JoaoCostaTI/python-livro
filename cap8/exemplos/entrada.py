def validaInteiro(msg, min, max):
    while True:
        try:
            v = int(input(msg))
            if v >= min and v <= max:
                return v
            else:
                print(f'Digite um numero entre {min} e {max}')
        except ValueError:
            print('Você deve digitar um numero inteiro! ')