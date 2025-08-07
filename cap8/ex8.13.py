"""
def opcoesValidas(msg, opcoesV):
    opcoes = opcoesV.lower()
    while True:
        escolha = input(msg)
        if escolha.lower() in opcoes:
            break
        print('Erro!. Digite novamente!\n')
    return escolha
"""
def valida_entrada(mensagem, opções_válidas):
    opções = opções_válidas.lower()
    while True:
        escolha = input(mensagem)
        if escolha.lower() in opções:
            break
        print("Erro: opção inválida. Redigite.\n")
    return escolha