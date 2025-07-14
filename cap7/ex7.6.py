s1 = 'AATTCGAA'
s2 = 'TG'
s3 = 'AC'


if len(s2) == len(s3):
    res = ""
    for letra in s1:
        pos = s2.find(letra)
        if pos != -1:
            res += s3[pos]
        else:
            res += letra
    if res == "":
        print('Todos caracteres foram removidos!')
    else:
        print(f'Os caracteres {s2} foram substituidos por {s3} em {s1}, gerando: {res}')

else:
    print('ERRO, as strings precisam ter o mesmo tamanho! ')