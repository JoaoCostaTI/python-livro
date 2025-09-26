import sys
import itertools

def imprimeBytes(imagem, bytesPorLinha = 16):
    for b in itertools.batched(imagem, bytesPorLinha):
        hexView = " ".join([f"{v:02x}" for v in b])
        tview = "".join([chr(v) if chr(v).isprintable() else "." for v in b])
        print(f'{hexView} {" " * 3 * (bytesPorLinha - len(b))} {tview}')

if __name__ == "__main__":
    with open(sys.argv[1], 'rb') as f:
        nMaximoBytes = int(sys.argv[2])
        bytesPorLinha = int(sys.argv[3])
        imagem = f.read(nMaximoBytes)
        imprimeBytes(imagem, bytesPorLinha)