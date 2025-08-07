def validaString(msg, lista):
    if msg in lista:
        print(f'{msg} foi encontrado! ')
    else:
        print(f'{msg} NÃO foi encontrado!')

validaString('maca', ['pera', 'uva', 'abacaxi', 'maca'])