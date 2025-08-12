import random


VIDA_JOGADOR = 100

arvore = random.randint(1,100)

print('Um alienigena está encondido atrás de uma árvore\nCada arvore foi numerada de 1 a 100.')

dificuldade = int(input('Qual dificuldade: \n1 - Fácil\n2 - Médio\n3 - Difícil\nSua opção: '))


if dificuldade == 1: 
    msg = 'Modo FÁCIL'
    VIDA_JOGADOR = 100
    dMin = 5
    dMax = 20
elif dificuldade == 2:
    msg = 'Modo MÉDIO'
    VIDA_JOGADOR = 80
    dMin = 10
    dMax = 25
else:
    msg = 'Modo DIFÍCIL'
    VIDA_JOGADOR = 75
    dMin = 20
    dMax = 30

print(msg)
while True:
        
        print(f'Vida do jogador:{VIDA_JOGADOR}')
        palpite = int(input('Digite seu palpite para encontrar a árvore: '))

        #condição de acerto!
        if palpite == arvore:
            print(f'Parabéns! Você acertou!\nArvore: {arvore}\nSeu palpite: {palpite}')
            break
        else:
            dano = random.randint(dMin, dMax)
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

