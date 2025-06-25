qtd_cigarros_dia = int(input('Quantos cigarros por dia: '))
qtd_anos_fumando = int(input('Quantos anos já fumou: '))
qtdDiasFumando = qtd_anos_fumando * 365

segundos_de_vida = 10 * 60 #Equivale a 10 minutos em segundos
cadaCigarro = qtd_cigarros_dia * segundos_de_vida
tempoDeVidaPerdido = qtdDiasFumando * cadaCigarro

dias = tempoDeVidaPerdido / (24*60*60)

print(int(dias))

