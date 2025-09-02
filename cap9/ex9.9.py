import sys

arquivos = sys.argv[1:]

print(type(arquivos))
print(arquivos)

for a in arquivos:
    print(f"\n--- Conteúdo de: {a} ---")
    with open(a, 'r', encoding="utf-8") as f:
        for l in f:
            print(l.strip())