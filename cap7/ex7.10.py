palavras = [
    "casa",
    "bola",
    "mangueira",
    "uva",
    "quiabo",
    "computador",
    "cobra",
    "lentilha",
    "arroz",
]

índice = int(input("Digite um numero:"))
palavra = palavras[(índice * 776) % len(palavras)]

print(palavra)