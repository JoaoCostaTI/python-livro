from time import sleep

pessoas = list()
def menuOpcoes():
    print('-' * 50)
    print(f'{"Sistema de cadastro de alunos".center(50)}')
    print('-' * 50)
    print('1 - Cadastrar Aluno\n2 - Listar Alunos\n3 - Atualizar Cadastro\n4 - Deletar registro\n0 - Sair do Programa')
    print('-' * 50)
def listagemAlunos():
    print('-' * 50)
    print(f'{"ID":<7}{"Nome":<15}')
    print('-' * 50)

#Menu Inicial
while True:
    sleep(0.7)
    menuOpcoes()
    opcao = int(input('Sua opção: '))

    if opcao == 0:
        sleep(0.7)
        print('Saindo do Programa...')
        break
    else:
        if opcao == 1:
            sleep(0.7)
            #Cadastro de Pessoas
            while True:
                #Nome
                pessoas.append(input('Nome Pessoa: '))
                while True:
                    op = str(input('Continuar? [S/N]')).strip().lower()

                    if op in ('s', 'n'):
                        break
                    else:
                        print('Escolha apenas [S/N]')

                if op == 'n':
                    break
        if opcao == 2:
            sleep(0.7)
            #Listando as pessoas
            listagemAlunos()
            for k, alunos in enumerate(pessoas):
                print(f'{k:<7}{alunos:<10}')

        if opcao == 3:
            sleep(0.7)
            #Alterando os dados de um aluno especifico
            #Listando as pessoas
            listagemAlunos()
            for k, alunos in enumerate(pessoas):
                print(f'{k:<7}{alunos:<10}')
            print('-' * 50)
            k = int(input('Alterar dado de qual Aluno? [Informar o ID]: '))

            if k >= len(pessoas):
                print(f'Erro, o Aluno {k} não existe na lista')
            else:  
                pessoas[k] = str(input('Novo nome do Aluno: '))

        if opcao == 4:
            sleep(0.7)
            listagemAlunos()
            for k, alunos in enumerate(pessoas):
                print(f'{k:<7}{alunos:<10}')
            print('-' * 50)
            # Excluindo registros
            k = int(input('Qual registro remover? [Inserir ID]'))
            if k >= len(pessoas):
                sleep(0.7)
                print(f'Erro! O aluno {k} não existe na lista')
            else:
                sleep(0.7)
                print(f'Registro {k} removido com sucesso! ')
                pessoas.pop(k)
            sleep(0.7)