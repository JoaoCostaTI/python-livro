materia1 = 8 
materia2 = 5 
materia3 = 7

#A expressão é:
materia1 >= 7 and materia2 >= 7 and materia3 >= 7

media = (materia1 + materia2 + materia3) / 3

situacao = ""

if media >= 7:
    situacao = 'Aprovado'
else: situacao = "Reprovado"

print(situacao)