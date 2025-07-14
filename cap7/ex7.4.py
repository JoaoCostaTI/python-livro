s = 'manteguno'
contagem = {}

for letra in s:
    if letra in contagem:
        contagem[letra] += 1
    else:
        contagem[letra] = 1

for k, v in contagem.items():
    print(f'{k} = {v}x')