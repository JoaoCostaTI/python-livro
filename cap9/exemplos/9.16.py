import json

with open('lista.json', 'r', encoding='UTF-8') as arquivo:
    turma = json.load(arquivo)

for aluno in turma:
    print(f"Nome: {aluno['nome']}")
    print(f"Notas: {aluno['notas']}")
    print(f"Média: {(sum(aluno['notas']) / (len(aluno['notas'])))}")
    print()