import sys

arquivos = sys.argv[1:]
arquivoFinal = ""

for arquivo in arquivos:
    arquivoFinal += f"Titulo: " + arquivo + "\n"
    with open(arquivo, 'r', encoding="utf-8") as a:
        for l in a:
            
            arquivoFinal += l.strip() + "\n"

print(arquivoFinal)

with open("arquivoFinalConcatenado.txt", 'w') as arquivo:
    arquivo.write(arquivoFinal)