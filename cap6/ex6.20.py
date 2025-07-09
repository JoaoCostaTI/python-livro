frase = str(input('Frase: '))
caracteres = {}

for letras in frase:
    if letras in caracteres:
        caracteres[letras] += 1
    else:
        caracteres[letras] = 1 
print(caracteres)