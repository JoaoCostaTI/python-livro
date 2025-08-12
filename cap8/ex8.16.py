import random


VIDA_JOGADOR = 100

arvore = random.randint(1,100)

print('Um alienigena está encondido atrás de uma árvore\nCada arvore foi numerada de 1 a 100.\nVocê tem 3 tentativas de advinhar em que arvore\no alienigena se esconde')

while True:
    print(f'Vida do jogador:{VIDA_JOGADOR}')
    palpite = int(input('Digite seu palpite para encontrar a árvore: '))

    #condição de acerto!
    if palpite == arvore:
        print(f'Parabéns! Você acertou!\nArvore: {arvore}\nSeu palpite: {palpite}')
        break
    else:
        dano = random.randint(5,20)
        print(f'Você errou! e recebeu {dano} dano')
        VIDA_JOGADOR -= dano

        #Pesquisa binária
        if palpite > arvore:
            print('Muito alto! ')
        else:
            print('Muito Baixo! ')

        if VIDA_JOGADOR <= 0:
            print('Você foi derrotado! GAME OVER!')
            break
    

