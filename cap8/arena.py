nomes  = ['Joao', 'Ana', 'Maria']

for tentativa in range(3):
    try:
        i = int(input('Digite o indice para verificar o nome: '))
        print(nomes[i])
    except ValueError:
        print('Digite apenas numeros')
        raise
    finally:
        print(f'Tentativa {tentativa + 1}')