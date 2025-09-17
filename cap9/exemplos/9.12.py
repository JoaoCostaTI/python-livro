import os
import sys

for raiz, diretorios, arquivos in os.walk(sys.argv[1]):
    print('\nCaminho: ', raiz)
    for d in diretorios:
        print(f"  {d}/")
    for f in arquivos:
        print(f"  {f}")
    print(f"{len(diretorios)} diretório(s), {len(arquivos)} arquivo(s)")





"""
import os.path

print(os.path.join("c:", "dados", 'programas'))
print(os.path.abspath(os.path.join("c:", 'dados', 'programas')))

caminho = 'i/j/k'
print(os.path.abspath(caminho))
print(os.path.basename(caminho))
print(os.path.dirname(caminho))
print(os.path.split(caminho))
print(os.path.splitext('arquivo.txt'))
print(os.path.splitdrive('C:/Windows'))
"""