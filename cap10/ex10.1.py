class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 2
        self.tamanho = 43
        self.marca = 'Sony'

tvJoao = Televisao()
tvMorning = Televisao()

#Atribuindo tamanho e marca diferente para as TV's
tvJoao.tamanho = 50
tvJoao.marca = 'AOC'

tvMorning.tamanho = 65
tvMorning.marca = "Samsung"

print(tvMorning.marca)
print(tvMorning.tamanho)
print()
print(tvJoao.marca)
print(tvJoao.tamanho)

