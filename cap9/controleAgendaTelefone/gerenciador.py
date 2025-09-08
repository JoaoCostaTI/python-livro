CONTATOS = []
NOME_ARQUIVO = "dados/contatos.txt"

def carregarContados():
    try:
        with open(NOME_ARQUIVO, 'r') as arquivo:
            for c in arquivo:
                dados = []
                contatoAtual = {}
                dados = c.strip().split(",")
                contatoAtual["nome"] =  dados[0]
                contatoAtual["telefone"] = dados[1]
                CONTATOS.append(contatoAtual)
            
    except FileNotFoundError:
        print('Arquivo não encontrado.')

def listarContatos():
    if len(CONTATOS) == 0:
        print('Lista vazia, cadastre ao menos 1 contato.')
    else:
        for v in CONTATOS:
            print('-' * 10)
            print(f"Nome: {v["nome"]}\nTelefone: {v["telefone"]}")
            print('-' * 10)

def salvarContatos():
    with open(NOME_ARQUIVO, 'w', encoding="utf-8") as arquivo:
        for c in CONTATOS:
            arquivo.write(f"{c['nome']},{c['telefone']}\n")
def adicionarContatos(nome, telefone):
    novoContato = {"nome":nome, "telefone": telefone}
    CONTATOS.append(novoContato)
    salvarContatos()
    print('Salvo com sucesso! ')

def removerContato(nome):
    contatoEncontrado = False
    for c in CONTATOS:
        if c['nome'] == nome:
            CONTATOS.remove(c)
            print('Removido com sucesso! ')
            contatoEncontrado = True
            salvarContatos()
            break
    if not contatoEncontrado:
       print('Nenhum usuário com este nome encontrado. ')

def atualizarContato(nome, telefone):
    contatoEncontrado = False
    for c in CONTATOS:
        if c['nome'] == nome:
            c['nome'] = nome
            c['telefone'] = telefone
            print('Atualizado com sucesso! ')
            contatoEncontrado = True
            salvarContatos()
            break
    if not contatoEncontrado:
        print('Contato não encontrado na lista! Cadastre esse usuário! ')
