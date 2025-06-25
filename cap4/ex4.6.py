dist = int(input('Distancia: '))

if dist <= 200:
    precoPassagem = dist * 0.50
else:
    precoPassagem = dist * 0.45
print(f'Com uma distancia de {dist}Km o preço da passagem será R${precoPassagem:.2f}')
