# Jogo da Forca

palavra = input('Digite a palavra secreta: ').lower().strip()

for x in range(100):
    print()
digitadas = []
acertos = []
erros = 0

while True:
    senha = ""
    for letra in palavra:
        senha += letra if letra in acertos else "."
    print(senha)
    if senha == palavra:
        print('Você acertou!')
        break
    tentativa = input('\nDigite uma letra: ').strip().lower()
    if tentativa in digitadas:
        print('Voce já tentou essa letra! ')
        continue
    else:
        digitadas += tentativa
        if tentativa in palavra:
            acertos += tentativa
        else:
            erros += 1
            print('Você errou!')
    print("X==:==\nX  :  ")
    print("X  O  " if erros >= 1 else "X")
    linha2 = ""
    if erros == 2:
        linha2 = " | "
    elif erros == 3:
        linha2 = " \| "
    elif erros == 4:
        linha2 = " \|/ "
    print(f"X{linha2}")
    linha3 = ""
    if erros == 5:
        linha3 += " /   "
    elif erros >= 6:
        linha3 += " /\ "
    print(f"X{linha3}")
    print('X\n==========')
    if erros == 6:
        print(f'Enforcado a palavra correta era: {palavra}')

        break