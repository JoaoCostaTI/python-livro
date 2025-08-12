import random

MAX_TENTATIVAS = 7


arvore = random.randint(1,100)

print('Um alienigena está encondido atrás de uma árvore\nCada arvore foi numerada de 1 a 100.\nVocê tem 3 tentativas de advinhar em que arvore\no alienigena se esconde')

for tentativa in range(1, MAX_TENTATIVAS+1):
    palpite = int(input(f'Árvore {tentativa}/{MAX_TENTATIVAS}: '))
    if palpite == arvore:
        print(f'Você acertou na {tentativa}\u00AA tentativa')
        break
    elif palpite > arvore:
        print('Muito alto!')
    else:
        print('Muito baixo!')
else:
    print('Você não conseguiu acertar! ')
    print(f'O alienigena estava na árvore {arvore}')