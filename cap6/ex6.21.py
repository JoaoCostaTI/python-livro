l1 = [1, 2, 6, 8]
l2 = [3, 6, 8, 9]

# Valores comuns nas duas listas:
print(f'{set(l1) & set(l2)}')

# Valores que só existem na primeira lista:
print(f'{set(l1) - set(l2)}')

# Valores que só existem na segunda lista:
print(f'{set(l2) - set(l1)}')

# Valores com elementos não repetidos das duas listas
print(f'{set(l2) ^ set(l1)}')

# Valores da primeira lista sem os elementos repetidos da segunda lista
print(f'{set(l1) - set(l2)}')