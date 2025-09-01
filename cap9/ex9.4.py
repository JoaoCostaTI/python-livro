import sys



if len(sys.argv) != 4:
    print('ERRO! Use o padrão: python nomeDoArquivo.py primeiroTXT segundoTXT nomeDoTerceiroTXT')
else:
    primeiro = open(sys.argv[1], 'r')
    segundo = open(sys.argv[2], 'r')
    saida = open(sys.argv[3], 'w')

    for pri in primeiro:
        saida.write(pri)
    saida.write(f"\n")
    for seg in segundo:
        saida.write(seg)
    
    primeiro.close()
    segundo.close()
    saida.close()