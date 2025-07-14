s1 = 'Algas e eletros'.strip().lower()
vogais = 'aeiou'
vogaisEncontradas = ''

qtd = 0

for v in s1:
    if v in vogais:
        vogaisEncontradas += v
        qtd += 1
print(f'Vogais encontradas: {vogaisEncontradas}\nQuantidade: {qtd}x')