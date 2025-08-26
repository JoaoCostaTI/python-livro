arquivo = open("numeros.txt", "w")

for linha in range(1,11):
    arquivo.write(f"Olá Mundo {linha}º\n")
arquivo.close()