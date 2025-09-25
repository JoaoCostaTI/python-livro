import json

alunos = {}

while nome := input('Nome do Aluno: '):
    notas = []        
    for c in range(4):
        n = float(input(f'{c+1}º nota: '))
        notas.append(n)

    alunos[nome] = notas

with open('notasAlunos.json','w', encoding='utf-8') as arquivo:
    json.dump(alunos, arquivo, indent=2, ensure_ascii=False)
