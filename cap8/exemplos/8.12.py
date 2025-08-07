def retangulo(larg, alt, caractere='*'):
    linha = caractere * larg
    for i in range(alt):
        print(linha)

retangulo(caractere='+', larg=8, alt=8)