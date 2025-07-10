antes = [1,2,5,6,9]
depois = [1,2,8,10]

cAntes = set(antes)
cDepois = set(depois)

print('Antes:', antes)
print('Depois:', depois)
print('Elementos que não mudaram:', cAntes & cDepois)
print('Novos elementos:', cDepois - cAntes )
print('Elementos que foram removidos:', cAntes - cDepois)