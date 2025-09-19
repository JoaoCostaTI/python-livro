with open("impares.txt", 'r') as impares, open("pares.txt", 'r') as pares, open("parImpar.txt", 'w') as parImpar:
    for linhaImpar, linhaPar in zip(impares, pares):
        parImpar.write(f"{linhaPar.strip()}\n")
        parImpar.write(f"{linhaImpar.strip()}\n")