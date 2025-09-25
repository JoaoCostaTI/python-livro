import json

tabelaDePrecos = {}

print('Criador de Tabela de Preços')
print('Digite um nome de produto em branco para terminar')
while produto := input('Nome do Produto: '):
    preco = input('Preço: ')
    tabelaDePrecos[produto] = preco
    print(tabelaDePrecos)

with open('precos.json', 'w', encoding='utf-8') as arquivo:
    json.dump(tabelaDePrecos, arquivo, indent=2, ensure_ascii=False)