import sys


def verificaPagina(arquivo, linha, pagina):
    if linha == LINHAS:
        rodape = f"= {NOME_DO_ARQUIVO} - Página: {pagina} ="
        arquivo.write(rodape.center(LARGURA - 1) + "\n")
        pagina += 1
        linha = 1
    return linha, pagina
def escreve(arquivo, linha, nlinhas, pagina):
    arquivo.write(linha + "\n")
    return verificaPagina(arquivo, nlinhas + 1, pagina)

if len(sys.argv) != 4:
    print("\nUSO: ex9.8.py arquivo largura linhas\n\n")
    sys.exit(1)

NOME_DO_ARQUIVO = sys.argv[1]
LARGURA = int(sys.argv[2])
LINHAS = int(sys.argv[3])

entrada = open(NOME_DO_ARQUIVO, encoding='utf-8')
saida = open("saida_paginada.txt", 'w', encoding="utf-8")

pagina = 1
linhas = 1

for linha in entrada.readlines():
    palavras = linha.rstrip().split(" ")
    linha = ""
    for p in palavras:
        p = p.strip()
        if len(linha) + len(p) + 1 > LARGURA:
            linhas, pagina = escreve(saida, linha, linhas, pagina)
            linha = ""
        linha += p + " "
    if linha != "":
        linhas, pagina = escreve(saida, linha, linhas, pagina)
while linhas != 1:
    linhas, pagina = escreve(saida, "", linhas, pagina)

entrada.close()
saida.close()