import sys
import itertools

def imprimeBytes(imagem, bytesPorLinha = 16):
    for b in itertools.batched(imagem, bytesPorLinha):
        hexView = " ".join([f"{v:02x}" for v in b])
        tview = "".join([chr(v) if chr(v).isprintable() else "." for v in b])
if __name__ == "_main_":
    with open(sys.argv[1], 'rb') as f:
        imagem = f.read()
        imprimeBytes()