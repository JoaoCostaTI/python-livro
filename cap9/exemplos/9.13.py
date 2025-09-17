import sys
from pathlib import Path
for raiz, diretorios, arquivos in Path(sys.argv[1]).walk():
    print("\nCaminho: ", raiz)
    for d in diretorios:
        print(f"  {d}/")
    for a in arquivos:
        print(f"  {a}")
    print(f"{len(diretorios)}, diretorio(s), {len(arquivos)}, arquivo(s)")
"""
mport pathlib
from pathlib import Path
caminho = Path("C:/Python")
print(caminho)
print(caminho.exists())
print(caminho.is_dir())
print(caminho.is_file())

caminho = Path('c:\\user\\user')
caminhoPai = caminho / "pai"
print(caminhoPai)
print(caminhoPai.parts)
print(caminhoPai.drive)
print(str(caminhoPai))
"""