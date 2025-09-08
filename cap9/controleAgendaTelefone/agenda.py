import sys
import gerenciador

gerenciador.carregarContados()

if sys.argv[1] == 'listar':
    gerenciador.listarContatos()

if len(sys.argv) == 4 and sys.argv[1] == 'adicionar':
    nome = sys.argv[2]
    telefone = sys.argv[3]
    gerenciador.adicionarContatos(nome, telefone)

if sys.argv[1] == 'remover':
    nome = sys.argv[2]
    gerenciador.removerContato(nome)
    
if sys.argv[1] == 'atualizar':
    nome = sys.argv[2]
    telefone = sys.argv[3]
    gerenciador.atualizarContato(nome, telefone)