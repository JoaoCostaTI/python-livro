t = [-10,-8,0,1,2,5,-2,-4]

maior = menor = t[0]
media = 0

for c in t:
    if c > maior:
        maior = c
    if c < menor:
        menor = c
    media += c

print(f'Maior temperatura: {maior}°C\nMenor temperatura: {menor}°C\nMédia de temperatura: {media/len(t):.1f}°C')